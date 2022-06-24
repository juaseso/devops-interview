from sqlalchemy import Column, String, Integer, ForeignKey

from app.db.base_class import Base


class Order(Base):
    __tablename__ = 'orders'

    customer = Column(Integer, ForeignKey('customers.id'))
    products = Column(String)
