from sqlalchemy import Column, Integer, String
from config.db import Base

class Product(Base):
    __tablename__ = 'products'
    id=Column(Integer, primary_key=True, index=True)
    email=Column(String, index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Integer)
    image=Column(String)
    category=Column(String)
    subCategory=Column(String)
    size=Column(String)