# telegram_bot/handlers/coin_handler.py
from aiogram import types, Router
from aiogram.filters import Command
from modules.coins.services import add_coin, list_coins, remove_coin
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from modules.accounts.models import User

router = Router()

# Add a coin for the user
@router.message(Command(commands=["add_coin"]))
async def add_user_coin(message: types.Message):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        db.close()
        return

    args = message.text.split()
    if len(args) < 2:
        await message.answer("Please provide the coin symbol. Usage: /add_coin <symbol>")
        db.close()
        return

    symbol = args[1]
    coin = add_coin(db, user.id, symbol)
    await message.answer(f"Coin added: {coin.symbol}")
    db.close()

# List all coins for the user
@router.message(Command(commands=["list_coins"]))
async def list_user_coins(message: types.Message):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        db.close()
        return

    coins = list_coins(db, user.id)
    if not coins:
        await message.answer("You have no coins.")
    else:
        coin_list = "\n".join([f"{c.symbol}" for c in coins])
        await message.answer(f"Your coins:\n{coin_list}")
    
    db.close()

# Remove a coin
@router.message(Command(commands=["remove_coin"]))
async def remove_user_coin(message: types.Message):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        db.close()
        return

    args = message.text.split()
    if len(args) < 2:
        await message.answer("Please provide the coin ID to remove. Usage: /remove_coin <coin_id>")
        db.close()
        return

    coin_id = int(args[1])
    success = remove_coin(db, coin_id)
    if success:
        await message.answer(f"Coin {coin_id} removed.")
    else:
        await message.answer(f"Coin {coin_id} not found.")
    
    db.close()
