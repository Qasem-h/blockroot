from sqlalchemy.orm import Session
from fastapi import HTTPException
from modules.subscription.models import Subscription
from modules.subscription.error_codes import SubscriptionErrorCodes
from modules.subscription.validators import SubscriptionValidator
from modules.subscription.utils import get_current_utc_time

# Create a new subscription for a user
def create_subscription(db: Session, user_id: int, plan_name: str) -> Subscription:
    if db.query(Subscription).filter(Subscription.user_id == user_id, Subscription.status == "active").first():
        raise HTTPException(status_code=400, detail=SubscriptionErrorCodes.SUBSCRIPTION_ALREADY_ACTIVE)

    validated_data = SubscriptionValidator(plan_name=plan_name).dict()

    new_subscription = Subscription(
        user_id=user_id,
        plan_name=validated_data["plan_name"],
        start_date=get_current_utc_time(),
    )
    
    db.add(new_subscription)
    db.commit()
    db.refresh(new_subscription)
    return new_subscription

# Get the active subscription for a user
def get_active_subscription(db: Session, user_id: int) -> Subscription:
    subscription = db.query(Subscription).filter(Subscription.user_id == user_id, Subscription.status == "active").first()
    if not subscription:
        raise HTTPException(status_code=404, detail=SubscriptionErrorCodes.SUBSCRIPTION_NOT_FOUND)
    return subscription

# Cancel a subscription
def cancel_subscription(db: Session, subscription_id: int) -> bool:
    subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail=SubscriptionErrorCodes.SUBSCRIPTION_NOT_FOUND)

    subscription.status = "canceled"
    subscription.end_date = get_current_utc_time()
    db.commit()
    return True
