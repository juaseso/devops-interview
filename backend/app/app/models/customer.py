from sqlalchemy import Column, String

from app.db.base_class import Base


class Customer(Base):
    __tablename__ = 'customers'

    firstname = Column(String)
    lastname = Column(String)
