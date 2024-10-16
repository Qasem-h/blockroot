from pydantic import BaseModel, Field, field_validator

class WalletValidator(BaseModel):
    blockchain: str = Field(..., min_length=3, max_length=30, description="Blockchain of the wallet")
    address: str = Field(..., min_length=20, max_length=42, description="Wallet address")

    @field_validator("blockchain")
    def validate_blockchain(cls, v):
        if not v.isalnum():
            raise ValueError("Blockchain name should only contain alphanumeric characters")
        return v

    @field_validator("address")
    def validate_address(cls, v):
        if not v.isalnum():
            raise ValueError("Wallet address should only contain alphanumeric characters")
        return v
