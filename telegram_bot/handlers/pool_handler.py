# telegram_bot/handlers/pool_handler.py
from aiogram import Router, types
from sqlalchemy.orm import Session
from modules.pools.services import add_pool, list_pools, remove_pool
from modules.accounts.models import User
from database.connection import SessionLocal
from aiogram.filters import Command

# Initialize the router
router = Router()

# Add a pool for the user
@router.message(Command(commands=["add_pool"]))
async def add_user_pool(message: types.Message):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        db.close()
        return

    # Split message text to extract blockchain and pool address
    args = message.text.split()
    if len(args) < 3:
        await message.answer("Please provide both blockchain and pool address. Usage: /add_pool <blockchain> <pool_address>")
        db.close()
        return

    blockchain = args[1]
    pool_address = args[2]

    pool = add_pool(db, user.id, blockchain, pool_address)
    await message.answer(f"Pool added: {pool.pool_address}")
    db.close()

# List all pools for the user
@router.message(Command(commands=["list_pools"]))
async def list_user_pools(message: types.Message):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        db.close()
        return

    pools = list_pools(db, user.id)
    if not pools:
        await message.answer("You have no pools.")
    else:
        pool_list = "\n".join([f"{p.blockchain}: {p.pool_address}" for p in pools])
        await message.answer(f"Your pools:\n{pool_list}")
    
    db.close()

# Remove a pool
@router.message(Command(commands=["remove_pool"]))
async def remove_user_pool(message: types.Message):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        db.close()
        return

    args = message.text.split()
    if len(args) < 2:
        await message.answer("Please provide the pool ID to remove. Usage: /remove_pool <pool_id>")
        db.close()
        return

    pool_id = int(args[1])
    success = remove_pool(db, pool_id)
    if success:
        await message.answer(f"Pool {pool_id} removed.")
    else:
        await message.answer(f"Pool {pool_id} not found.")
    
    db.close()
