from pydantic import BaseModel, Field

class SubscriptionValidator(BaseModel):
    plan_name: str = Field(..., min_length=3, max_length=30, description="Name of the subscription plan")

    @classmethod
    def validate_plan_name(cls, v):
        allowed_plans = ["Free", "Premium", "Pro"]
        if v not in allowed_plans:
            raise ValueError(f"Invalid subscription plan. Allowed plans are: {', '.join(allowed_plans)}")
        return v
