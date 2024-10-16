from pydantic import BaseModel, Field, field_validator

class UserValidator(BaseModel):
    telegram_id: int = Field(..., description="Telegram ID", gt=0)
    username: str = Field(None, min_length=3, max_length=30)
    first_name: str = Field(None)
    last_name: str = Field(None)

    @field_validator("username")
    def validate_username(cls, v):
        if v and " " in v:
            raise ValueError("Username cannot contain spaces")
        return v.lower().strip()
