from sqlalchemy import Column, String, Float

from app.db.base_class import Base


class Product(Base):
    __tablename__ = 'products'

    name = Column(String)
    cost = Column(Float)
