from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
# from database import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
	_tablename_ = "Product"

	id = Column(Integer, primary_key= True, index =True)
	name = Column(String(100), index= True)
	price = Column(float)
	quentity = Column(Integer, index= True)

class Order(Base):
	_tablename_ = "Order"
	
	product_id = Column(Integer, primary_key= True)
	price = Column(float, index = True)
	fee = Column(float)
	quentity = Column(Integer)
	total = Column(Integer)
	status = Column(String(100))