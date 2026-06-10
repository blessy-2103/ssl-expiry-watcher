# src/engine.py

def incident_engine(days_left):
    if days_left == -1:
        return "BROKEN"
    elif days_left <= 7:
        return "P1 - CRITICAL"
    elif days_left <= 30:
        return "P2 - WARNING"
    else:
        return "P3 - OK"


def renewal_engine(days_left):
    if days_left <= 30 and days_left != -1:
        return "RENEWAL_TRIGGERED"
    return "NO_ACTION"


def service_status(days_left):
    if days_left == -1:
        return "BROKEN"
    elif days_left <= 30:
        return "WARNING"
    return "HEALTHY"