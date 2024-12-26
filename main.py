from fastapi import FastAPI
from api.user_api import user_router
from api.car_api import car_router
from database import Base, engine

app = FastAPI(docs_url='/')
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(car_router)
