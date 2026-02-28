from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import engine,get_db
from ..schemas import MealEntryCreate,MealEntryResponse ,DailySummaryResponse
from ..services.calorie_service import (create_meal_entry,get_daily_summary) 
from datetime import date

router=APIRouter(
    prefix="/calories",
    tags=["Calories"]
)

@router.post("/meal/add",response_model=MealEntryResponse)
def add_meal(data:MealEntryCreate,db:Session=Depends(get_db)):
    return create_meal_entry(db,data)

@router.get("/summary", response_model=DailySummaryResponse)
def get_summary(date: date, db: Session = Depends(get_db)):
    return get_daily_summary(db, date)

