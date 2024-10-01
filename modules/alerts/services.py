from sqlalchemy.orm import Session
from modules.alerts.models import GasAlert

def create_gas_alert(db: Session, user_id: int, threshold: float):
    alert = GasAlert(user_id=user_id, threshold=threshold)
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert

def list_gas_alerts(db: Session, user_id: int):
    return db.query(GasAlert).filter(GasAlert.user_id == user_id).all()

def remove_gas_alert(db: Session, alert_id: int):
    alert = db.query(GasAlert).filter(GasAlert.id == alert_id).first()
    if not alert:
        return False
    db.delete(alert)
    db.commit()
    return True
