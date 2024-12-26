from database import get_db
from database.models import *

def create_user_db(name, phone_number, email, city, password):
    db = next(get_db())
    new_user = User(name=name, phone_number=phone_number, email=email,
                    city=city, password=password)
    db.add(new_user)
    db.commit()
    return True

def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users

def get_exact_user_db(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=user_id).first()
    return exact_user

def change_user_db(user_id, change_info, new_info):
    db = next(get_db())
    update_user = db.query(User).filter_by(id=user_id).first()
    if update_user:
        if change_info == 'name':
            update_user.name = new_info
        elif change_info == 'phone_number':
            update_user.phone_number = new_info
        elif change_info == 'email':
            update_user.email = new_info
        elif change_info == 'city':
            update_user.city = new_info
        elif change_info == 'password':
            update_user.password = new_info
        else:
            return False
        db.commit()
        return True
    return False

def delete_user_db(user_id):
    db = next(get_db())
    delete_user = db.query(User).filter_by(id=user_id).first()
    if delete_user:
        db.delete(delete_user)
        db.commit()
        return True
    return False
