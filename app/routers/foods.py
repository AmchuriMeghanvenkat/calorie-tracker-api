from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import engine,get_db
from ..schemas import FoodCreate,FoodResponse
from ..services.calorie_service import (create_food,get_all_foods)

router=APIRouter(
    prefix="/foods",
    tags=["Foods"]
)

@router.post("/add",response_model=FoodResponse)
def add_food(data:FoodCreate,db:Session=Depends(get_db)):
    return create_food(db,data)

@router.get("/all",response_model=list[FoodResponse])
def get_foods(db:Session=Depends(get_db)):
    return get_all_foods(db)