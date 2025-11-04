from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# SQLite URL by default; can be overridden by env var DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./mcp.db")

# For SQLite we need check_same_thread=False for the default driver when using threads
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
