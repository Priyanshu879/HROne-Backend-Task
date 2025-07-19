from fastapi import APIRouter, Query
from utils.database import db
from utils.schema import Product, NewProductSchema, ProductResponse
from typing import List, Optional
from bson import Regex

router = APIRouter()

@router.post("/products", status_code=201)
async def add_product(product: NewProductSchema):
    product_data = product.model_dump()
    result = await db.products.insert_one(product_data)
    product_data["_id"] = result.inserted_id
    return {"id": str(product_data["_id"])}

@router.get("/products", status_code=200)
async def get_products(
    name: Optional[str] = Query(None, description="Search term for product names"),
    size: Optional[str] = Query(None, description="Search term for product sizes"),
    limit: Optional[int] = Query(10, ge=1, le=100, description="Number of products to return"),
    offset: Optional[int] = Query(0, ge=0, description="Offset for pagination")
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}

    if size:
        query["sizes.size"] = {"$regex": size, "$options": "i"}

    products_res = db.products.find(query, {"sizes":0}).skip(offset).limit(limit)
    products = [Product.to_json(product) async for product in products_res]

    return {
        "data": products,
        "page": {
            "next": limit + offset,
            "limit": limit,
            "previous": offset - limit
        }
    }