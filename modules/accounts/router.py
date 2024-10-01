from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from modules.accounts.services import create_user_from_telegram, get_user_by_telegram_id

router = APIRouter()

# Get user by Telegram ID
@router.get("/users/{telegram_id}")
def get_user(telegram_id: int, db: Session = Depends(get_db)):
    return get_user_by_telegram_id(db, telegram_id)

# Create a new user
@router.post("/users/")
def create_user(telegram_id: int, username: str, first_name: str = None, last_name: str = None, db: Session = Depends(get_db)):
    return create_user_from_telegram(db, telegram_id, username, first_name, last_name)
