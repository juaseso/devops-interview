from typing import Optional

from pydantic import BaseModel


class MyBaseModel(BaseModel):
    id: Optional[int]
