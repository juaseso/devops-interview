import uuid

import sqlalchemy as sa
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:
    id = sa.Column(Integer, primary_key=True)
