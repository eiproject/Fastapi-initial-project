from datetime import datetime
from pytz import timezone


def get_now() -> datetime:
    return datetime.now(timezone('Asia/Jakarta'))
