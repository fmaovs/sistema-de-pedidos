# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Configuración de la URL de conexión
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('MYSQL_ADDON_USER')}:{os.getenv('MYSQL_ADDON_PASSWORD')}"
    f"@{os.getenv('MYSQL_ADDON_HOST')}:{os.getenv('MYSQL_ADDON_PORT')}/{os.getenv('MYSQL_ADDON_DB')}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
