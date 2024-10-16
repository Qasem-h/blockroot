from sqlalchemy.orm import Session
from fastapi import HTTPException
from modules.accounts.models import User
from modules.accounts.error_codes import UserErrorCodes
from modules.accounts.validators import UserValidator
from modules.accounts.utils import get_current_utc_time

# Get a user by Telegram ID
def get_user_by_telegram_id(db: Session, telegram_id: int) -> User:
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=UserErrorCodes.USER_NOT_FOUND)
    return user

# Create a new user from Telegram data
def create_user_from_telegram(db: Session, telegram_id: int, username=None, first_name=None, last_name=None) -> User:
    user_data = {
        "telegram_id": telegram_id,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "is_active": True
    }

    validated_data = UserValidator(**user_data).dict()
    if db.query(User).filter(User.username == validated_data["username"]).first():
        raise HTTPException(status_code=400, detail=UserErrorCodes.USERNAME_ALREADY_TAKEN)

    new_user = User(
        **validated_data,
        created_at=get_current_utc_time(),
        updated_at=get_current_utc_time()
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Update user data
def update_user(db: Session, telegram_id: int, **data) -> User:
    user = get_user_by_telegram_id(db, telegram_id)
    for key, value in data.items():
        setattr(user, key, value)
    user.updated_at = get_current_utc_time()
    db.commit()
    db.refresh(user)
    return user
