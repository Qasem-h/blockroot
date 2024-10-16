from sqlalchemy.orm import Session
from fastapi import HTTPException
from modules.alerts.models import Alert
from modules.alerts.error_codes import AlertErrorCodes

# Create a new alert
def create_alert(db: Session, user_id: int, alert_type: str, threshold_value: float):
    if threshold_value <= 0:
        raise HTTPException(status_code=400, detail=AlertErrorCodes.INVALID_THRESHOLD_VALUE)
    
    new_alert = Alert(user_id=user_id, alert_type=alert_type, threshold_value=threshold_value)
    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)
    return new_alert

# Get alerts for a user
def get_user_alerts(db: Session, user_id: int):
    return db.query(Alert).filter(Alert.user_id == user_id).all()

# Update an alert
def update_alert(db: Session, alert_id: int, threshold_value: float):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail=AlertErrorCodes.ALERT_NOT_FOUND)

    alert.threshold_value = threshold_value
    db.commit()
    db.refresh(alert)
    return alert

# Delete an alert
def delete_alert(db: Session, alert_id: int):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail=AlertErrorCodes.ALERT_NOT_FOUND)

    db.delete(alert)
    db.commit()
