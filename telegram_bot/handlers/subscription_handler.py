from aiogram import types
from sqlalchemy.orm import Session
from modules.subscription.services import create_subscription, get_active_subscription
from modules.accounts.models import User  # Assuming User is in accounts/models.py
from database.connection import SessionLocal

async def subscribe_user(message: types.Message, plan_type: str):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        return
    
    if get_active_subscription(db, user.id):
        await message.answer("You already have an active subscription.")
    else:
        create_subscription(db, user.id, plan_type)
        await message.answer(f"Your {plan_type} subscription has been activated.")
    
    db.close()

# No more handler registration in this file
