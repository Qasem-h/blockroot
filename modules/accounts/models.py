from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    username = Column(String, index=True)
    first_name = Column(String)  # Add first_name attribute
    last_name = Column(String)   # Add last_name attribute (optional)
    email = Column(String, nullable=True)  # Email is now optional
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    # Relationship to wallets
    wallets = relationship("Wallet", back_populates="user")
    gas_alerts = relationship("GasAlert", back_populates="user")
