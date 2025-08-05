import os
import pymysql.cursors

#DB_HOST = os.environ.get('DB_HOST', '10.135.124.35')
#DB_USER = os.environ.get('DB_USER')
#DB_PASSWORD = os.environ.get('DB_PASSWORD')
#DB_NAME = os.environ.get('DB_NAME', 'test1')  # optional default

CONNECTION = pymysql.connect(
    #host=DB_HOST,
    host='10.135.124.35',
    #user=DB_USER,
    user='newuser',
    #password=DB_PASSWORD,
    password='Pass@1234',
    #db=DB_NAME,
    db='test1',
    port=3306,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
