from collections import defaultdict
from datetime import datetime, timedelta

request_tracker = defaultdict(list)

MAX_REQUESTS = 20

def check_rate_limit(session_id):

    now = datetime.now()

    one_hour_ago = now - timedelta(hours=1)

    request_tracker[session_id] = [
        timestamp
        for timestamp in request_tracker[session_id]
        if timestamp > one_hour_ago
    ]

    if len(request_tracker[session_id]) >= MAX_REQUESTS:
        return False

    request_tracker[session_id].append(now)

    return True