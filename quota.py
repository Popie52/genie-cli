import json
import os
from datetime import datetime, timedelta

QUOTA_FILE = "quota_block.json"

def save_quota_block():
    """Save current time as last quota hit."""
    with open(QUOTA_FILE, "w") as f:
        json.dump({"blocked_until": (datetime.now() + timedelta(hours=24)).isoformat()}, f)

def is_quota_blocked():
    """Check if quota block is still active."""
    if os.path.exists(QUOTA_FILE):
        with open(QUOTA_FILE, "r") as f:
            data = json.load(f)
            blocked_until = datetime.fromisoformat(data["blocked_until"])
            if datetime.now() < blocked_until:
                return True, blocked_until
    return False, None
