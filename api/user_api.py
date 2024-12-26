from fastapi import APIRouter
from database.user_service import *
from api import result_message

user_router = APIRouter(prefix='/user', tags=['Пользователи'])

@user_router.post('/create_user')
async def create_user(name: str, phone_number: str, email: str,
                      city: str, password: str):
    result = create_user_db(name=name, phone_number=phone_number, email=email,
                    city=city, password=password)
    result_message(result)

@user_router.get('/get_all_users')
async def get_all_users():
    result = get_all_users_db()
    result_message(result)

@user_router.get('/get_exact_user')
async def get_exact_user(user_id: int):
    result = get_exact_user_db(user_id=user_id)
    result_message(result)

@user_router.put('/change_user')
async def change_user(user_id: int, change_info: str, new_info: str):
    result = change_user_db(user_id=user_id, change_info=change_info,
                            new_info=new_info)
    result_message(result)

@user_router.delete('/delete_user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id=user_id)
    result_message(result)
