from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from database.base import Base


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    plan_type = Column(String, nullable=False)  # e.g., "monthly", "yearly"
    is_active = Column(Boolean, default=True)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
