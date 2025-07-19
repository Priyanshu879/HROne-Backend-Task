from fastapi import FastAPI
from routes.products_route import router as products_router
from routes.order_route import router as order_router

app = FastAPI()

app.include_router(products_router, prefix="/api")
app.include_router(order_router, prefix="/api")

