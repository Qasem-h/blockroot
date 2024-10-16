from pydantic import BaseModel, Field, field_validator

class PoolValidator(BaseModel):
    pool_name: str = Field(..., min_length=3, max_length=100, description="Name of the pool")
    blockchain: str = Field(..., min_length=3, max_length=30, description="Blockchain where the pool exists")

    @field_validator("pool_name")
    def validate_pool_name(cls, v):
        if not v.strip():
            raise ValueError("Pool name cannot be empty or whitespace.")
        return v.strip()

    @field_validator("blockchain")
    def validate_blockchain(cls, v):
        if not v.isalnum():
            raise ValueError("Blockchain name should only contain alphanumeric characters.")
        return v.strip()
