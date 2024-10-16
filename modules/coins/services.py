from sqlalchemy.orm import Session
from fastapi import HTTPException
from modules.coins.models import Coin
from modules.coins.error_codes import CoinErrorCodes
from modules.coins.utils import get_current_utc_time, format_coin_name, format_coin_symbol
from modules.coins.validators import CoinValidator

# Add a new coin
def add_coin(db: Session, symbol: str, name: str) -> Coin:
    formatted_symbol = format_coin_symbol(symbol)
    formatted_name = format_coin_name(name)

    if db.query(Coin).filter(Coin.symbol == formatted_symbol).first():
        raise HTTPException(status_code=400, detail=CoinErrorCodes.COIN_ALREADY_EXISTS)

    validated_data = CoinValidator(symbol=formatted_symbol, name=formatted_name).dict()

    new_coin = Coin(
        symbol=validated_data["symbol"],
        name=validated_data["name"],
        created_at=get_current_utc_time(),
        updated_at=get_current_utc_time()
    )
    
    db.add(new_coin)
    db.commit()
    db.refresh(new_coin)
    return new_coin

# Get all coins
def get_all_coins(db: Session):
    coins = db.query(Coin).all()
    return [{"symbol": format_coin_symbol(coin.symbol), "name": format_coin_name(coin.name)} for coin in coins]

# Remove a coin by ID
def remove_coin(db: Session, coin_id: int) -> bool:
    coin = db.query(Coin).filter(Coin.id == coin_id).first()
    if not coin:
        raise HTTPException(status_code=404, detail=CoinErrorCodes.COIN_NOT_FOUND)

    db.delete(coin)
    db.commit()
    return True
