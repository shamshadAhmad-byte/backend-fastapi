from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str
    price: int
    image: str
    category: str
    subCategory: str
    size: str

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    image: str
    category: str
    subCategory: str
    size: str

    class Config:
        from_attributes = True