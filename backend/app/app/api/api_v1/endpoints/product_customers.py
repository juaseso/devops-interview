import io
from typing import Any

import pandas as pd
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import StreamingResponse

from app.api import deps
from app.services.data_process import get_product_customers

router = APIRouter()


@router.get("")
def read_product_customers(db: Session = Depends(deps.get_db)) -> Any:
    """
    Returns a list of product id with a list of customers which have bought that product
    """
    return get_product_customers(db=db)


@router.get("/download", response_class=StreamingResponse)
def download_product_customers_file(db: Session = Depends(deps.get_db)) -> Any:
    """
    Returns a list of product id with a list of customers which have bought that product in a csv file
    """
    product_customers_df = pd.DataFrame(get_product_customers(db=db))
    stream = io.StringIO()
    product_customers_df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=product_customers.csv"
    return response
