from typing import Optional

# Shared properties
from .base_model import MyBaseModel


class CustomerBase(MyBaseModel):
    firstname: Optional[str]
    lastname: Optional[str]


class Customer(CustomerBase):
    firstname: str
    lastname: str
