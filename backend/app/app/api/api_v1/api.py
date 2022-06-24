from fastapi import APIRouter

from app.api.api_v1.endpoints import customer_ranking, order_prices, product_customers

api_router = APIRouter()

api_router.include_router(customer_ranking.router, prefix="/customerRanking", tags=["Customer Ranking"])
api_router.include_router(order_prices.router, prefix="/orderPrices", tags=["Order Prices"])
api_router.include_router(product_customers.router, prefix="/productCustomers", tags=["Product Customers"])
