import pymysql.cursors

CONNECTION = pymysql.connect(
    host='10.135.124.35',
    user='newuser',
    password='Pass@1234',
    port=3306,
    db='test1',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
