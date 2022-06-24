from app import schemas
from app.crud.base import CRUDBase
from app.models import Customer


class CRUDCustomer(CRUDBase[Customer, schemas.Customer]):
    pass


customer = CRUDCustomer(Customer)
