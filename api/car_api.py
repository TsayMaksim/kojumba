from fastapi import APIRouter
from database.car_service import *
from api import result_message

car_router = APIRouter(prefix='/car', tags=['Машины'])

@car_router.post('/create_car')
async def create_car(brand: str, model: str, car_type: str, condition: str,
                     year: int, price: float, mileage_km: int, fuel: str,
                     transmission: str, color: str, description: str):
    result = create_car_db(brand=brand, model=model, car_type=car_type, condition=condition,
                  year=year, price=price, mileage_km=mileage_km, fuel=fuel,
                  transmission=transmission, color=color, description=description)
    result_message(result)

@car_router.get('/get_all_cars')
async def get_all_cars():
    result = get_all_cars_db()
    result_message(result)

@car_router.get('/get_exact_car')
async def get_exact_car(car_id: int):
    result = get_exact_car_db(car_id=car_id)
    result_message(result)

@car_router.put('/change_car')
async def change_car(car_id: int, change_info: str, new_info: str):
    result = change_car_db(car_id=car_id, change_info=change_info,
                           new_info=new_info)
    result_message(result)

@car_router.delete('/delete_car')
async def delete_car(car_id: int):
    result = delete_car_db(car_id=car_id)
    result_message(result)
