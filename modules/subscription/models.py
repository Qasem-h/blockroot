from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database.base import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    plan_name = Column(String, nullable=False)  # Plan name (e.g., Free, Premium)
    status = Column(String, default="active")  # Subscription status (active, canceled)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    end_date = Column(DateTime, nullable=True)  # When the subscription expires

    # Relationship with User
    user = relationship("User", back_populates="subscription")
