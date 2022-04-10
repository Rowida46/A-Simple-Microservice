from datetime import date
from pydantic import BaseModel

"""The line orm_mode = True allows the app to take ORM objects and translate them into responses 
    automatically. This automation saves us frommanually taking data out of ORM, 
    making it into a dictionary, then loading it in with Pydantic
"""

class Product(BaseModel):
    id: int
    name: str
    quentity: int
    price: float

    class Config:
        orm_mode = True


class Order(BaseModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str  # pending, completed, refunded

    class Config:
        orm_mode = True