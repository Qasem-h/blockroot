from sqlalchemy.orm import Session
from fastapi import HTTPException
from modules.wallets.models import Wallet
from modules.wallets.error_codes import WalletErrorCodes
from modules.wallets.utils import format_wallet_address

# Add a new wallet for a user
def add_wallet(db: Session, user_id: int, blockchain: str, address: str) -> Wallet:
    if db.query(Wallet).filter(Wallet.address == address).first():
        raise HTTPException(status_code=400, detail=WalletErrorCodes.WALLET_ALREADY_EXISTS)

    new_wallet = Wallet(user_id=user_id, blockchain=blockchain, address=address)
    db.add(new_wallet)
    db.commit()
    db.refresh(new_wallet)
    return new_wallet

# List all wallets for a user
def list_wallets(db: Session, user_id: int):
    wallets = db.query(Wallet).filter(Wallet.user_id == user_id).all()
    return [{"blockchain": wallet.blockchain, "address": format_wallet_address(wallet.address)} for wallet in wallets]

# Remove a wallet by ID (soft deletion)
def remove_wallet(db: Session, wallet_id: int) -> bool:
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail=WalletErrorCodes.WALLET_NOT_FOUND)

    wallet.is_deleted = True
    db.commit()
    return True
