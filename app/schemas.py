from pydantic import BaseModel
from datetime import date
from enum import Enum

        
        
class FoodBase(BaseModel):
    name:str
    calories_per_100gm:float
class FoodCreate(FoodBase):
    pass
class FoodResponse(FoodBase):
    id:int
    class config:
        from_attributes=True
        
class MealType(str,Enum):
    breakfast="Breakfast"
    lunch="Lunch"
    dinner="Dinner"
    snack="Snack"
class MealEntryBase(BaseModel):
    food_name:str
    grams:float
    meal_type:MealType
    date:date
class MealEntryCreate(MealEntryBase):
    pass
class MealEntryResponse(MealEntryBase):
    id:int
    food_name:str
    grams:float
    meal_type:str
    date:date
    calculated_calories:float
    class config:
        from_attributes=True
        
class MealTypeSummary(BaseModel):
    meal_type:str
    calories:float
class DailySummaryResponse(BaseModel):
    date:date
    meal_totals:list[MealTypeSummary]
    total_calories:float
