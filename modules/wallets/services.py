from sqlalchemy.orm import Session
from modules.wallets.models import Wallet
from modules.wallets.error_codes import WalletErrorCodes
from fastapi import HTTPException

def add_wallet(db: Session, user_id: int, blockchain: str, address: str):
    # Check if wallet already exists
    existing_wallet = db.query(Wallet).filter(Wallet.address == address).first()
    if existing_wallet:
        raise HTTPException(status_code=400, detail=WalletErrorCodes.WALLET_ALREADY_EXISTS)

    wallet = Wallet(user_id=user_id, blockchain=blockchain, address=address)
    db.add(wallet)
    db.commit()
    db.refresh(wallet)
    return wallet

def list_wallets(db: Session, user_id: int):
    return db.query(Wallet).filter(Wallet.user_id == user_id).all()

def remove_wallet(db: Session, wallet_id: int):
    wallet = db.query(Wallet).get(wallet_id)
    if not wallet:
        raise HTTPException(status_code=404, detail=WalletErrorCodes.WALLET_NOT_FOUND)
    
    db.delete(wallet)
    db.commit()
    return True
