from typing import Optional

# Shared properties
from app.schemas.base_model import MyBaseModel


class OrderBase(MyBaseModel):
    customer: Optional[int]
    products: Optional[str]


class Order(OrderBase):
    customer: int
    products: str
