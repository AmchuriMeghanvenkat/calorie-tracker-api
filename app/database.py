from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.orm import Session


    
DATABASE_URL="mysql+pymysql://root:Meghan%40429@127.0.0.1:3306/calorie_db"

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
engine=create_engine(
    DATABASE_URL,
    echo=True
)
SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base=declarative_base()