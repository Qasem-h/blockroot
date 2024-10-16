from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database.base import Base

class Pool(Base):
    __tablename__ = "pools"

    id = Column(Integer, primary_key=True, index=True)
    pool_name = Column(String, nullable=False)  # Name of the pool (e.g., Uniswap Pool)
    blockchain = Column(String, nullable=False)  # Blockchain where the pool exists (e.g., Ethereum)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationship with UserPoolTracking
    users_tracking = relationship("UserPoolTracking", back_populates="pool")


class UserPoolTracking(Base):
    __tablename__ = "user_pool_tracking"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    pool_id = Column(Integer, ForeignKey('pools.id'), nullable=False)
    added_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Timestamp for when the user started tracking the pool
    track_frequency = Column(String, nullable=True)  # How frequently the user wants to track the pool

    user = relationship("User", back_populates="pool_tracking")
    pool = relationship("Pool", back_populates="users_tracking")
