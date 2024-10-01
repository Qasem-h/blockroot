from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.settings import settings

# SQLAlchemy database URL (ensure your settings contain the correct database URL)
SQLALCHEMY_DATABASE_URL = settings.database_url

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal is the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
