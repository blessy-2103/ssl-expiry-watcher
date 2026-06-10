import ssl
import socket
import datetime


def get_ssl_expiry(hostname):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:

                cert = ssock.getpeercert()

                if not cert:
                    return {
                        "domain": hostname,
                        "expiry_date": None,
                        "days_left": -1,
                        "error": "No certificate returned"
                    }

                expiry = cert.get("notAfter")

                if not expiry:
                    return {
                        "domain": hostname,
                        "expiry_date": None,
                        "days_left": -1,
                        "error": "notAfter missing"
                    }

                expiry_dt = datetime.datetime.strptime(
                    expiry,
                    "%b %d %H:%M:%S %Y %Z"
                )

                days_left = (expiry_dt - datetime.datetime.utcnow()).days

                return {
                    "domain": hostname,
                    "expiry_date": expiry_dt,
                    "days_left": days_left
                }

    except Exception as e:
        return {
            "domain": hostname,
            "expiry_date": None,
            "days_left": -1,
            "error": str(e)
        }