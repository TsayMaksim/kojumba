from database import Base
from sqlalchemy import (Column, Integer, String, Float, Text, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    city = Column(String, nullable=False)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    car_type = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    mileage_km = Column(Integer, nullable=False)
    fuel = Column(String, nullable=False)
    transmission = Column(String, nullable=False)
    color = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    date = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship(User, lazy="subquery")