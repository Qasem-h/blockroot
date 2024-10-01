from pydantic import BaseModel, Field, field_validator

class GasAlertValidator(BaseModel):
    blockchain: str = Field(..., description="Blockchain type (e.g., Ethereum, BSC)")
    threshold_price: float = Field(..., description="Gas price threshold in gwei")

    @field_validator("threshold_price")
    def validate_threshold_price(cls, v):
        if v <= 0:
            raise ValueError("Threshold price must be greater than zero")
        return v
