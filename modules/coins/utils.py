from datetime import datetime, timezone

# Utility to get the current time in UTC
def get_current_utc_time():
    return datetime.now(timezone.utc)

# Format coin name for display
def format_coin_name(name: str) -> str:
    """Format coin name for display."""
    return name.title()

# Format coin symbol for consistency
def format_coin_symbol(symbol: str) -> str:
    """Format coin symbol for consistency."""
    return symbol.upper()
