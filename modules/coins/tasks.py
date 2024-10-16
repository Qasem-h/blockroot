from fastapi import BackgroundTasks
from sqlalchemy.orm import Session
from modules.coins.services import check_price_alerts

def schedule_price_checking(background_tasks: BackgroundTasks, db: Session):
    background_tasks.add_task(check_price_alerts, db)
