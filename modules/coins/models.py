from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database.base import Base

class Coin(Base):
    __tablename__ = "coins"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, nullable=False)  # Coin symbol (e.g., BTC, ETH)
    name = Column(String, nullable=False)  # Full name of the coin (e.g., Bitcoin)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationship with UserCoinTracking
    users_tracking = relationship("UserCoinTracking", back_populates="coin")


class UserCoinTracking(Base):
    __tablename__ = "user_coin_tracking"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    coin_id = Column(Integer, ForeignKey('coins.id'), nullable=False)
    added_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Timestamp for when the user started tracking the coin
    track_frequency = Column(String, nullable=True)  # How frequently the user wants to track the coin

    user = relationship("User", back_populates="coin_tracking")
    coin = relationship("Coin", back_populates="users_tracking")
