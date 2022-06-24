import io
from typing import Any

import pandas as pd
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.api import deps
from app.services.data_process import get_customer_ranking

router = APIRouter()


@router.get("/")
def read_customer_ranking(db: Session = Depends(deps.get_db)) -> Any:
    """
    Returns a list of customers, ordered by how much have they spent
    """
    return get_customer_ranking(db=db)


@router.get("/download", response_class=StreamingResponse)
def download_customer_ranking_file(db: Session = Depends(deps.get_db)):
    """
    Returns a list of customers, ordered by how much have they spent in a csv file
    """
    customer_ranking_df = pd.DataFrame(get_customer_ranking(db=db))
    stream = io.StringIO()
    customer_ranking_df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=customer_ranking.csv"
    return response
