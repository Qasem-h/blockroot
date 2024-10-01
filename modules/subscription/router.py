from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from modules.subscription.services import create_subscription, get_active_subscription

router = APIRouter()

# Create a new subscription
@router.post("/subscribe/")
def subscribe_user(user_id: int, plan_type: str, db: Session = Depends(get_db)):
    return create_subscription(db, user_id, plan_type)

# Get the active subscription for a user
@router.get("/subscription/{user_id}")
def get_subscription(user_id: int, db: Session = Depends(get_db)):
    return get_active_subscription(db, user_id)
