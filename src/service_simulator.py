import random
from datetime import datetime, timedelta


def simulate_service_status(days_left):
    """
    Simulates whether a service is working or broken based on SSL expiry.
    """

    if days_left == -1:
        return {
            "status": "BROKEN",
            "reason": "SSL ERROR / CERT NOT FOUND"
        }

    if days_left <= 0:
        return {
            "status": "DOWN",
            "reason": "CERTIFICATE EXPIRED → SERVICE FAILURE"
        }

    if days_left <= 7:
        return {
            "status": "DEGRADED",
            "reason": "CERT EXPIRING VERY SOON → RISK OF FAILURE"
        }

    if days_left <= 30:
        return {
            "status": "WARNING",
            "reason": "CERT EXPIRING SOON → MONITOR CLOSELY"
        }

    return {
        "status": "HEALTHY",
        "reason": "SSL VALID"
    }