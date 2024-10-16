from datetime import datetime, timezone

# Utility to get the current time in UTC
def get_current_utc_time():
    return datetime.now(timezone.utc)

# Format user's full name
def format_user_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}".strip() or "Unknown"
