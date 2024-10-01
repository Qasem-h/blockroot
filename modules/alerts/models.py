from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

class GasAlert(Base):
    __tablename__ = "gas_alerts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    threshold = Column(Float, nullable=False)

    # Relationship to User
    user = relationship("User", back_populates="gas_alerts")
