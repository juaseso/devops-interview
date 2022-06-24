from typing import Optional

# Shared properties
from .base_model import MyBaseModel


class ProductBase(MyBaseModel):
    name: Optional[str]
    cost: Optional[float]


class Product(ProductBase):
    name: str
    cost: float
