def format_gas_alert_message(blockchain: str, threshold: float) -> str:
    """Format a gas alert message for a given blockchain and threshold."""
    return f"Gas alert set for {blockchain} at {threshold} gwei."
