from sqlalchemy.orm import Session
from app.models import Food,MealEntry   
from app.schemas import FoodCreate,MealEntryCreate  
from fastapi import HTTPException
from sqlalchemy import func
from datetime import date

def create_food(db:Session,data:FoodCreate)->Food:
    food=db.query(Food).filter(func.lower(Food.name)==data.name.lower()).first()
    if food:
        raise HTTPException(status_code=400,detail="Food already exists")
    new_food=Food(
        name=data.name.strip().title(),
        calories_per_100gm=data.calories_per_100gm
    )
    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    
    return new_food 

def get_all_foods(db:Session):
    return db.query(Food).all()


def create_meal_entry(db:Session,data:MealEntryCreate)->MealEntry:
    food=db.query(Food).filter(Food.name==data.food_name).first()
    if not food:
        raise HTTPException(status_code=404,detail="Food not Found")
    calculated=(food.calories_per_100gm/100)*data.grams
    entry=MealEntry(
        food_id=food.id,
        grams=data.grams,
        meal_type=data.meal_type,
        date=data.date,
        calculated_calories=calculated
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    
    return  {
        "id":entry.id,
        "food_name":food.name,
        "grams":entry.grams,
        "meal_type":entry.meal_type,
        "date":entry.date,
        "calculated_calories":entry.calculated_calories
    }
        


def get_daily_summary(db: Session, selected_date: date):

    # 1️⃣ Group calories by meal type
    grouped = db.query(MealEntry.meal_type,func.sum(MealEntry.calculated_calories)).filter(MealEntry.date == selected_date).group_by(MealEntry.meal_type).all()

    # 2️⃣ Get total calories for full day
    total = db.query(func.sum(MealEntry.calculated_calories)).filter(MealEntry.date == selected_date).scalar()

    if total is None:
        total = 0

    meal_totals = []

    for meal_type, calories in grouped:
        meal_totals.append({
            "meal_type": meal_type,
            "calories": calories
        })

    return {
        "date": selected_date,
        "meal_totals": meal_totals,
        "total_calories": total
    }