def calculate_subscription_end_date(plan_type: str) -> str:
    """Calculate the subscription end date based on the plan type (monthly/yearly)."""
    from datetime import datetime, timedelta

    start_date = datetime.utcnow()
    if plan_type == "monthly":
        return (start_date + timedelta(days=30)).isoformat()
    elif plan_type == "yearly":
        return (start_date + timedelta(days=365)).isoformat()
    else:
        raise ValueError("Invalid subscription plan type")
