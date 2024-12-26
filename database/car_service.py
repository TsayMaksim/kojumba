from database import get_db
from database.models import *

def create_car_db(brand, model, car_type, condition, year, price, mileage_km,
                  fuel, transmission, color, description):
    db = next(get_db())
    new_car = Car(brand=brand, model=model, car_type=car_type, condition=condition,
                  year=year, price=price, mileage_km=mileage_km, fuel=fuel,
                  transmission=transmission, color=color, description=description)
    db.add(new_car)
    db.commit()
    return True

def get_all_cars_db():
    db = next(get_db())
    all_cars = db.query(Car).all()
    return all_cars

def get_exact_car_db(car_id):
    db = next(get_db())
    exact_car = db.query(Car).filter_by(id=car_id).first()
    return exact_car

def change_car_db(car_id, change_info, new_info):
    db = next(get_db())
    update_car = db.query(Car).filter_by(id=car_id).first()
    if update_car:
        if change_info == 'brand':
            update_car.brand = new_info
        elif change_info == 'model':
            update_car.model = new_info
        elif change_info == 'car_type':
            update_car.car_type = new_info
        elif change_info == 'condition':
            update_car.condition = new_info
        elif change_info == 'year':
            update_car.year = new_info
        elif change_info == 'price':
            update_car.price = new_info
        elif change_info == 'mileage_km':
            update_car.mileage_km = new_info
        elif change_info == 'fuel':
            update_car.fuel = new_info
        elif change_info == 'transmission':
            update_car.transmission = new_info
        elif change_info == 'color':
            update_car.color = new_info
        elif change_info == 'description':
            update_car.description = new_info
        else:
            return False
        db.commit()
        return True
    return False

def delete_car_db(car_id):
    db = next(get_db())
    delete_car = db.query(Car).filter_by(id=car_id).first()
    if delete_car:
        db.delete(delete_car)
        db.commit()
        return True
    return False
