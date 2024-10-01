from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    blockchain = Column(String, index=True)
    address = Column(String, unique=True, index=True)

    # Relationship to User
    user = relationship("User", back_populates="wallets")
