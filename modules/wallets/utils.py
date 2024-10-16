def format_wallet_address(address: str) -> str:
    """
    Formats wallet address for display purposes by showing the first 6 and last 4 characters.
    Example: 0x1234567890abcdef -> 0x1234...cdef
    """
    return f"{address[:6]}...{address[-4:]}"
