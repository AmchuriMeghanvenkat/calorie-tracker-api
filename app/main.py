from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI
from .database import engine
from . import models
from .routers import calories,foods

app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="templates")
models.Base.metadata.create_all(bind=engine)
app.include_router(calories.router)
app.include_router(foods.router)

@app.get('/')
def home(request:Request):
    return templates.TemplateResponse("index.html",{"request": request})
