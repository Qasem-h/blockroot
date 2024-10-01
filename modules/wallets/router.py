from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from modules.wallets.services import add_wallet, list_wallets, remove_wallet

router = APIRouter()

# Add a new wallet
@router.post("/add/")
def add_user_wallet(user_id: int, blockchain: str, address: str, db: Session = Depends(get_db)):
    return add_wallet(db, user_id, blockchain, address)

# List all wallets for a user
@router.get("/list/{user_id}")
def list_user_wallets(user_id: int, db: Session = Depends(get_db)):
    return list_wallets(db, user_id)

# Remove a wallet by its ID
@router.delete("/remove/{wallet_id}")
def remove_user_wallet(wallet_id: int, db: Session = Depends(get_db)):
    return remove_wallet(db, wallet_id)
