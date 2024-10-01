from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from modules.subscription.models import Subscription

def create_subscription(db: Session, user_id: int, plan_type: str):
    """Create a new subscription for a user."""
    start_date = datetime.utcnow()
    if plan_type == "monthly":
        end_date = start_date + timedelta(days=30)
    elif plan_type == "yearly":
        end_date = start_date + timedelta(days=365)
    
    subscription = Subscription(
        user_id=user_id,
        plan_type=plan_type,
        start_date=start_date.isoformat(),
        end_date=end_date.isoformat()
    )
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return subscription

def get_active_subscription(db: Session, user_id: int):
    """Check if a user has an active subscription."""
    current_date = datetime.utcnow().isoformat()
    return db.query(Subscription).filter(
        Subscription.user_id == user_id,
        Subscription.is_active == True,
        Subscription.end_date >= current_date
    ).first()
