from aiogram import types
from sqlalchemy.orm import Session
from modules.wallets.services import add_wallet, list_wallets, remove_wallet
from modules.accounts.models import User
from database.connection import SessionLocal
from fastapi import HTTPException

# Add a wallet for the user
async def add_user_wallet(message: types.Message):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        db.close()
        return

    # Split message text to extract blockchain and wallet address
    args = message.text.split()
    if len(args) < 3:
        await message.answer("Please provide both blockchain and wallet address. Usage: /add_wallet <blockchain> <address>")
        db.close()
        return

    blockchain = args[1]
    address = args[2]

    try:
        wallet = add_wallet(db, user.id, blockchain, address)
        await message.answer(f"Wallet added: {wallet.address}")
    except HTTPException as e:
        if e.status_code == 400 and e.detail == 'wallet_already_exists':
            await message.answer(f"A wallet with the address {address} on {blockchain} already exists.")
        else:
            await message.answer("An error occurred while adding the wallet. Please try again later.")
    finally:
        db.close()

# List all wallets for the user
async def list_user_wallets(message: types.Message):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        db.close()
        return

    wallets = list_wallets(db, user.id)
    if not wallets:
        await message.answer("You have no wallets.")
    else:
        wallet_list = "\n".join([f"{w.blockchain}: {w.address}" for w in wallets])
        await message.answer(f"Your wallets:\n{wallet_list}")
    
    db.close()

# Remove a wallet
async def remove_user_wallet(message: types.Message):
    db: Session = SessionLocal()
    telegram_id = message.from_user.id
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    if not user:
        await message.answer("You need to register first by starting the bot.")
        db.close()
        return

    args = message.text.split()
    if len(args) < 2:
        await message.answer("Please provide the wallet ID to remove. Usage: /remove_wallet <wallet_id>")
        db.close()
        return

    wallet_id = int(args[1])
    success = remove_wallet(db, wallet_id)
    if success:
        await message.answer(f"Wallet {wallet_id} removed.")
    else:
        await message.answer(f"Wallet {wallet_id} not found.")
    
    db.close()
