from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = os.environ.get("DATABASE_URL")
# print("DB_URL:", DATABASE_URL)  # Check if it's actually loading


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
