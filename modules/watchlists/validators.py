from pydantic import BaseModel, Field

class WatchlistValidator(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Name of the watchlist")

    @classmethod
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError("Watchlist name cannot be empty")
        return v.strip()
