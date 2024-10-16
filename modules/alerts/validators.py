from pydantic import BaseModel, Field

class AlertValidator(BaseModel):
    alert_type: str = Field(..., description="Type of the alert")
    threshold_value: float = Field(..., description="Threshold value", ge=0)

    @classmethod
    def validate_alert_type(cls, v):
        allowed_types = ["Gas Fee", "Price Pump", "Transaction Alert"]
        if v not in allowed_types:
            raise ValueError(f"Invalid alert type. Allowed types are: {', '.join(allowed_types)}")
        return v
