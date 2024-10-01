from aiogram import types
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from modules.alerts.services import create_gas_alert, list_gas_alerts, remove_gas_alert
from modules.accounts.models import User

# Add a gas alert for the user
async def add_gas_alert(message: types.Message, threshold: float):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        return
    
    create_gas_alert(db, user.id, threshold)
    await message.answer(f"Gas price alert set at {threshold} GWEI.")
    
    db.close()

# List gas alerts for the user
async def list_gas_alerts(message: types.Message):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        return
    
    alerts = list_gas_alerts(db, user.id)
    if not alerts:
        await message.answer("You have no gas alerts.")
    else:
        alert_list = "\n".join([f"Threshold: {a.threshold} GWEI" for a in alerts])
        await message.answer(f"Your gas alerts:\n{alert_list}")
    
    db.close()

# Remove a gas alert
async def remove_gas_alert(message: types.Message, alert_id: int):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        return
    
    success = remove_gas_alert(db, alert_id)
    if success:
        await message.answer(f"Gas alert {alert_id} removed.")
    else:
        await message.answer(f"Gas alert {alert_id} not found.")
    
    db.close()
