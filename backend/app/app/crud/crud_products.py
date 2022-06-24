from sqlalchemy.orm import Session

from app import schemas
from app.crud.base import CRUDBase
from app.models import Product


class CRUDProduct(CRUDBase[Product, schemas.Product]):
    pass

product = CRUDProduct(Product)
