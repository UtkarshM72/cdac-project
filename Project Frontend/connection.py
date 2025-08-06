import os
import pymysql.cursors

DB_HOST = os.environ.get('DB_HOST', '10.135.124.35')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME', 'test1')  # optional default

CONNECTION = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    db=DB_NAME,
    port=3306,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
