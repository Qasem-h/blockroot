from datetime import datetime, timezone

# Utility to get the current time in UTC
def get_current_utc_time():
    return datetime.now(timezone.utc)
