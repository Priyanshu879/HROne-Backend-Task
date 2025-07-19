from pydantic import BaseModel
from typing import List

class NewProductSchema(BaseModel):
    name: str
    price: float
    sizes: List

class ProductResponse(NewProductSchema):
    id: str

class NewOrderSchema(BaseModel):
    userId: str
    items: List

class OrderResponse(NewOrderSchema):
    id: str

class Product:
    @staticmethod
    def to_json(product):
        return {
            "id": str(product["_id"]),
            "name": product["name"],
            "price": product["price"],
            "sizes": product["sizes"]
        }
        
class Order:
    @staticmethod
    def to_json(order):
        return {
            "id": str(order["_id"]),
            "userId": order["userId"],
            "items": order["items"]
        }