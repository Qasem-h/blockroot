from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database.base import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    blockchain = Column(String, nullable=False)
    address = Column(String, unique=True, nullable=False)
    is_deleted = Column(Boolean, default=False)  # Soft deletion flag

    # Relationship with UserWalletTracking
    users_tracking = relationship("UserWalletTracking", back_populates="wallet")


class UserWalletTracking(Base):
    __tablename__ = "user_wallet_tracking"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    wallet_id = Column(Integer, ForeignKey('wallets.id'), nullable=False)
    alert_threshold = Column(Float, nullable=True)
    alert_method = Column(String, default="telegram")
    added_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Added timestamp for tracking
    track_frequency = Column(String, nullable=True)  # Custom tracking settings

    user = relationship("User", back_populates="wallet_tracking")
    wallet = relationship("Wallet", back_populates="users_tracking")
