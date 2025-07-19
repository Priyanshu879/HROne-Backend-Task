from fastapi import APIRouter, Query
from utils.database import db
from utils.schema import Order, NewOrderSchema, OrderResponse
from typing import List, Optional
from bson import ObjectId

router = APIRouter()

@router.post("/orders",status_code=201) 
async def add_order(order: NewOrderSchema):
    order_data = order.model_dump()
    result = await db.orders.insert_one(order_data)
    order_data["_id"] = result.inserted_id
    return {
        "id": str(order_data["_id"])
    }

@router.get("/orders/{user_id}", status_code=200)
async def get_orders(user_id: str, 
    limit: Optional[int] = Query(10, ge=1, le=100, description="Number of products to return"),
    offset: Optional[int] = Query(0, ge=0, description="Offset for pagination")):
    
    result = db.orders.find({"userId": user_id}).skip(offset).limit(limit)

    orders = []

    async for order in result:
        order_id = str(order.get("_id"))
        items = order.get("items", [])
        res_items = []
        price = 0.0

        for p_id in items:
            prod = await db.products.find_one({"_id":ObjectId(p_id)})

            if prod:
                prod_price = prod.get("price", 0)
                qty = 1

                item = {
                    "productDetails": {
                        "name": prod.get("name"),
                        "id":   str(prod.get("_id"))
                    },
                    "qty": qty
                }

                res_items.append(item)
                price += prod_price * qty

        orders.append({
            "id": order_id,
            "items": res_items,
            "total": price
        })

        return {
            "data": orders,
            "page": {
                "next": limit + offset,
                "limit": limit,
                "previous": offset - limit
            }
        }