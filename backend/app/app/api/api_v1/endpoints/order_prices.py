import io
from typing import Any

import pandas as pd
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import StreamingResponse

from app.api import deps
from app.services.data_process import get_order_prices

router = APIRouter()


@router.get("/")
def read_order_prices(db: Session = Depends(deps.get_db)) -> Any:
    """
    Returns a list of orders with precalculated total amount
    """
    return get_order_prices(db=db)


@router.get("/download", response_class=StreamingResponse)
def download_order_prices_file(db: Session = Depends(deps.get_db)) -> Any:
    """
    Returns a list of orders with precalculated total amount in a csv file
    """
    order_prices_df = pd.DataFrame(get_order_prices(db=db))
    stream = io.StringIO()
    order_prices_df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=order_prices.csv"
    return response
