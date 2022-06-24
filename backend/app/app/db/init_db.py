import json

import pandas as pd
from sqlalchemy.orm import Session

from app import schemas, crud
from app.db import base  # noqa: F401
from app.db.base_class import Base
from app.db.session import engine


def get_table_data(csv_file):
    raw_data = pd.read_csv(csv_file)
    return json.loads(raw_data.to_json(orient='records'))


def load_customers(db: Session):
    for row in get_table_data('app/db/customers.csv'):
        crud.customer.create(db=db, obj_in=schemas.Customer(**row))


def load_orders(db: Session):
    for row in get_table_data('app/db/orders.csv'):
        crud.order.create(db=db, obj_in=schemas.Order(**row))


def load_products(db: Session):
    for row in get_table_data('app/db/products.csv'):
        crud.product.create(db=db, obj_in=schemas.Product(**row))


def init_db(db: Session) -> None:
    try:
        Base.metadata.drop_all(bind=engine)
    except:
        pass

    Base.metadata.create_all(bind=engine)

    # Initialize tables using csv datasets
    load_customers(db)
    load_products(db)
    load_orders(db)
