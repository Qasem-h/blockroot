from sqlalchemy.orm import Session
from fastapi import HTTPException
from modules.watchlists.models import Watchlist
from modules.watchlists.error_codes import WatchlistErrorCodes
from modules.watchlists.validators import WatchlistValidator
from modules.watchlists.utils import get_current_utc_time

# Create a new watchlist
def create_watchlist(db: Session, user_id: int, name: str) -> Watchlist:
    if db.query(Watchlist).filter(Watchlist.name == name, Watchlist.user_id == user_id).first():
        raise HTTPException(status_code=400, detail=WatchlistErrorCodes.WATCHLIST_ALREADY_EXISTS)
    
    validated_data = WatchlistValidator(name=name).dict()

    new_watchlist = Watchlist(
        name=validated_data["name"],
        user_id=user_id,
        created_at=get_current_utc_time(),
        updated_at=get_current_utc_time()
    )
    
    db.add(new_watchlist)
    db.commit()
    db.refresh(new_watchlist)
    return new_watchlist

# Get watchlists for a user
def get_user_watchlists(db: Session, user_id: int):
    return db.query(Watchlist).filter(Watchlist.user_id == user_id).all()

# Update a watchlist
def update_watchlist(db: Session, watchlist_id: int, name: str) -> Watchlist:
    watchlist = db.query(Watchlist).filter(Watchlist.id == watchlist_id).first()
    if not watchlist:
        raise HTTPException(status_code=404, detail=WatchlistErrorCodes.WATCHLIST_NOT_FOUND)

    watchlist.name = name
    watchlist.updated_at = get_current_utc_time()
    db.commit()
    db.refresh(watchlist)
    return watchlist

# Delete a watchlist
def delete_watchlist(db: Session, watchlist_id: int) -> bool:
    watchlist = db.query(Watchlist).filter(Watchlist.id == watchlist_id).first()
    if not watchlist:
        raise HTTPException(status_code=404, detail=WatchlistErrorCodes.WATCHLIST_NOT_FOUND)

    db.delete(watchlist)
    db.commit()
    return True
