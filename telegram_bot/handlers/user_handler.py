from aiogram import types
from sqlalchemy.orm import Session
from modules.accounts.services import create_user_from_telegram, get_user_by_telegram_id
from database.connection import SessionLocal
from fastapi import HTTPException
from modules.accounts.error_codes import UserErrorCodes

# Function to start the bot and register the user if not found
async def start_bot(message: types.Message):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    username = message.from_user.username or "Unknown"
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    
    email = None  # Optional email, not requested explicitly for now

    try:
        # Try to get the user by Telegram ID
        user = get_user_by_telegram_id(db, telegram_id=telegram_id)
    except HTTPException as e:
        if e.status_code == 404:
            # If user not found, create a new user
            user = create_user_from_telegram(
                db, telegram_id=telegram_id, username=username, first_name=first_name, last_name=last_name, email=email
            )
            await message.answer(f"Welcome, {user.first_name}! You have been registered.")
        else:
            raise e
    else:
        # If the user exists, send a welcome back message
        await message.answer(f"Welcome back, {user.first_name}!")

    db.close()
