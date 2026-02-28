from sqlalchemy import Column,Integer,String,Date,Float,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship



class Food(Base):
    __tablename__="foods"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(255),unique=True,nullable=False)
    calories_per_100gm=Column(Float,nullable=False)
    
    meals=relationship('MealEntry',back_populates="food")

class MealEntry(Base):
    __tablename__="meal_entry"
    
    id=Column(Integer,primary_key=True,index=True)
    food_id=Column(Integer,ForeignKey("foods.id"),nullable=False)
    grams=Column(Float,nullable=False)
    meal_type=Column(String(50),nullable=False)
    date=Column(Date,nullable=False)
    calculated_calories=Column(Float,nullable=False)
    
    food=relationship("Food",back_populates="meals")
