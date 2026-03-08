from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.userRoute import userRouter
from routes.productRoute import productRouter
from config.db import Base, engine

app=FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(userRouter)
app.include_router(productRouter)

@app.get('/')
def home():
    return {"message":"Hello World"}

