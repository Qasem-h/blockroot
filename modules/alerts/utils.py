def format_alert_details(alert):
    """
    Formats alert details for display.
    """
    status = "Active" if alert.active else "Inactive"
    return f"Alert Type: {alert.alert_type}, Threshold: {alert.threshold_value}, Status: {status}"
