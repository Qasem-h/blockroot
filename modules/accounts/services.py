# modules/accounts/services.py
from sqlalchemy.orm import Session
from modules.accounts.models import User
from modules.accounts.error_codes import UserErrorCodes
from fastapi import HTTPException

def create_user_from_telegram(db: Session, telegram_id: int, username: str, first_name: str, last_name: str, email: str = None):
    """Create a new user in the database using Telegram info."""
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail=UserErrorCodes.USERNAME_ALREADY_TAKEN)
    
    user = User(
        telegram_id=telegram_id,
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_telegram_id(db: Session, telegram_id: int):
    """Fetch a user by their Telegram ID."""
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=UserErrorCodes.USER_NOT_FOUND)
    return user
