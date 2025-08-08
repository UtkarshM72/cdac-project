import os
import pymysql.cursors
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Environment variables
#DB_HOST = os.environ.get('DB_HOST', '10.135.124.35')
#DB_USER = os.environ.get('DB_USER')
#DB_PASSWORD = os.environ.get('DB_PASSWORD')
#DB_NAME = os.environ.get('DB_NAME', 'test1')

# Retry logic: up to 5 attempts, exponential backoff (2s, 4s, 8s...)
@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(pymysql.MySQLError),
    reraise=True
)
def get_connection():
    return pymysql.connect(
        #host=DB_HOST,
        #user=DB_USER,
        #password=DB_PASSWORD,
        #db=DB_NAME,
        host = '10.135.124.35',
        user='newuser',
        password='Pass@1234',
        db='test1',
        port=3306,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# Optional: eager connection on import (or call get_connection() in app.py)
try:
    CONNECTION = get_connection()
except pymysql.MySQLError as e:
    print(f"Failed to connect to DB after retries: {e}")
    CONNECTION = None  # or raise, depending on your app's needs
