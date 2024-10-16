from fastapi import APIRouter

router = APIRouter()

@router.get("/list")
async def list_alerts():
    # Logic to list alerts
    return {"alerts": []}

@router.post("/add")
async def add_alert(alert_data: dict):
    # Logic to add an alert
    return {"message": "Alert added"}

@router.delete("/{alert_id}")
async def remove_alert(alert_id: int):
    # Logic to remove an alert
    return {"message": f"Alert {alert_id} removed"}
