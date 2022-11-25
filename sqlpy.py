import mysql.connector

dbconfig = {
    'host': '127.0.0.1',
    'user': 'user',
    'password': 'pass',
    'database': 'vsearchlogDB',
}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()


_SQL = """insert into log(phrase, letters, ip, browser_string, results)
values (%s, %s, %s, %s, %s)"""
cursor.execute(_SQL, ('hitch-hiker', 'aeiou', '127.0.0.1', 'Safari', 'set()'))
conn.commit()

_SQL_ = """select * from log"""
cursor.execute(_SQL_)
res = cursor.fetchall()
for row in res:
    print(row)


cursor.close()
conn.close()

