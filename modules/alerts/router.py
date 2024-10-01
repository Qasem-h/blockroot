from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from modules.alerts.services import create_gas_alert, list_gas_alerts, remove_gas_alert

router = APIRouter()

# Add a new gas price alert
@router.post("/gas-alert/")
def add_gas_alert(user_id: int, threshold: float, db: Session = Depends(get_db)):
    return create_gas_alert(db, user_id, threshold)

# List all gas price alerts for a user
@router.get("/gas-alerts/{user_id}")
def list_gas_alerts(user_id: int, db: Session = Depends(get_db)):
    return list_gas_alerts(db, user_id)

# Remove a gas price alert by its ID
@router.delete("/gas-alert/{alert_id}")
def remove_gas_alert(alert_id: int, db: Session = Depends(get_db)):
    return remove_gas_alert(db, alert_id)
