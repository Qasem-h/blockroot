from pydantic import BaseModel, Field, field_validator

class SubscriptionValidator(BaseModel):
    plan_type: str = Field(..., description="Subscription plan type (monthly/yearly)")

    @field_validator("plan_type")
    def validate_plan_type(cls, v):
        if v not in ["monthly", "yearly"]:
            raise ValueError("Invalid plan type")
        return v
