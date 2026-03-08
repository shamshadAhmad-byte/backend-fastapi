from models.productModel import Product
from fastapi import HTTPException



def create_products(product,email, db):
    new_product=Product(
        name=product.name,
        description=product.description,
        price=product.price,
        image=product.image,
        category=product.category,
        subCategory=product.subCategory,
        size=product.size,
        email=email
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"id": new_product.id, "name": new_product.name, "description": new_product.description, "price": new_product.price, "image": new_product.image, "category": new_product.category, "subCategory": new_product.subCategory, "size": new_product.size}

def update_product(product_id,email, product, db):
    existProduct=db.query(Product).filter(Product.id==product_id).first()
    if not existProduct:
        raise HTTPException(status_code=404, detail="product not found")
    if existProduct.email!=email:
        raise HTTPException(status_code=401, detail="unauthorized")
    existProduct.name = product.name
    existProduct.description = product.description
    existProduct.price = product.price
    existProduct.image = product.image
    existProduct.category = product.category
    existProduct.subCategory = product.subCategory
    existProduct.size = product.size
    db.commit()
    db.refresh(existProduct)
    return {"id": existProduct.id, "name": existProduct.name, "description": existProduct.description, "price": existProduct.price, "image": existProduct.image, "category": existProduct.category, "subCategory": existProduct.subCategory, "size": existProduct.size}

def delete_product(product_id,email, db):
    existProduct=db.query(Product).filter(Product.id==product_id).first()
    if(not existProduct):
        raise HTTPException(status_code=404, detail="product not found")
    if existProduct.email != email:
        raise HTTPException(status_code=401, detail="unauthorized")
    db.delete(existProduct)
    db.commit()
    return {"message": "product deleted successfully"}

def get_product_by_id(product_id,email, db):
    existProduct=db.query(Product).filter(Product.id==product_id).first()
    if not existProduct:
        raise HTTPException(status_code=404, detail="product not found")
    if existProduct.email != email:
        raise HTTPException(status_code=401, detail="unauthorized")
    return existProduct

def get_all_products(email,db):
    products=db.query(Product).filter(Product.email==email).all()
    return products
