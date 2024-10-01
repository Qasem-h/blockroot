from pydantic import BaseModel, Field, field_validator
import re

class WalletValidator(BaseModel):
    blockchain: str = Field(..., description="Blockchain type (e.g., Ethereum, BSC)")
    address: str = Field(..., description="Wallet address")

    @field_validator("address")
    def validate_ethereum_address(cls, v, values):
        if values.get('blockchain') == "Ethereum" or values.get('blockchain') == "BSC":
            if not re.match(r"^0x[a-fA-F0-9]{40}$", v):
                raise ValueError("Invalid Ethereum/BSC address format")
        return v

    @field_validator("address")
    def validate_solana_address(cls, v, values):
        if values.get('blockchain') == "Solana":
            if not re.match(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$", v):
                raise ValueError("Invalid Solana address format")
        return v
