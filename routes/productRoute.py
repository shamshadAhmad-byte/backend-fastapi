from fastapi import APIRouter, Depends, HTTPException 
from schemas.productSchema import Product, ProductResponse
from config.db import get_db
from sqlalchemy.orm import Session
from controller.productController import (
    create_products,
    update_product as update_product_controller,
    delete_product as delete_product_controller,
    get_product_by_id,
    get_all_products,
)
from utils.auth import get_current_user

productRouter=APIRouter()

@productRouter.post("/product/create", status_code=201, response_model=ProductResponse)
def create_product(product: Product,email:str=Depends(get_current_user), db: Session=Depends(get_db)):
    return create_products(product,email, db)

@productRouter.put("/product/update/{product_id}", status_code=200, response_model=ProductResponse)
def update_product(product_id: int,product: Product,email:str=Depends(get_current_user),  db: Session=Depends(get_db)):
    if not product_id:
        raise HTTPException(status_code=400, detail="product id is required")
    return update_product_controller(product_id,email, product, db)

@productRouter.delete("/product/delete/{product_id}",status_code=200, response_model=dict)
def delete_product(product_id: int,email:str=Depends(get_current_user), db: Session=Depends(get_db)):
    if(not product_id):
        raise HTTPException(status_code=400, detail="product id is required")
    return delete_product_controller(product_id,email, db)

@productRouter.get("/product/{product_id}", status_code=200, response_model=ProductResponse)
def get_product(product_id: int,email:str=Depends(get_current_user), db: Session=Depends(get_db)):
    if not product_id:
        raise HTTPException(status_code=400, detail="product id is required")
    return get_product_by_id(product_id, email,db)

@productRouter.get("/products", status_code=200, response_model=list[ProductResponse])
def get_products(email:str=Depends(get_current_user), db: Session=Depends(get_db)):
    return get_all_products(email,db)
