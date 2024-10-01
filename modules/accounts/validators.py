from pydantic import BaseModel, Field, field_validator

class UserValidator(BaseModel):
    telegram_id: int = Field(..., description="Telegram ID of the user", gt=0)
    username: str = Field(..., min_length=3, max_length=30, description="Telegram username")
    first_name: str = Field(None, description="First name of the user")
    last_name: str = Field(None, description="Last name of the user")

    @field_validator("username")
    def validate_username(cls, v):
        if " " in v:
            raise ValueError("Username should not contain spaces")
        if not v.isalnum():
            raise ValueError("Username should only contain alphanumeric characters")
        return v

    @field_validator("telegram_id")
    def validate_telegram_id(cls, v):
        if v <= 0:
            raise ValueError("Telegram ID must be greater than 0")
        return v
