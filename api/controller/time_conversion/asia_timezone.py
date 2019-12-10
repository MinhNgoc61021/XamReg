import pytz
from datetime import datetime

vntz = pytz.timezone('Asia/Ho_Chi_Minh')


def set_custom_log_time():
    return datetime.now(tz=vntz).strftime("%Y-%m-%d %H:%M:%S")
