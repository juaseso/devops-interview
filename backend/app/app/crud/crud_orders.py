from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas
from app.crud.base import CRUDBase
from app.models import Order


class CRUDOrder(CRUDBase[Order, schemas.Order]):
    def create(self, db: Session, *, obj_in: schemas.Order) -> Order:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Order(**obj_in_data)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


order = CRUDOrder(Order)
