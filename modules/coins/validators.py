from pydantic import BaseModel, Field, field_validator

class CoinValidator(BaseModel):
    symbol: str = Field(..., min_length=1, max_length=10, description="Symbol of the coin (e.g., BTC)")
    name: str = Field(..., min_length=1, max_length=50, description="Name of the coin (e.g., Bitcoin)")

    @field_validator("symbol", pre=True)
    def validate_symbol(cls, v):
        v = v.strip()  # Trim whitespace
        if not v.isupper():
            raise ValueError("Symbol should be uppercase.")
        return v

    @field_validator("name", pre=True)
    def validate_name(cls, v):
        v = v.strip()  # Trim whitespace
        if not all(x.isalpha() or x.isspace() for x in v):
            raise ValueError("Name should contain only alphabetic characters and spaces.")
       
