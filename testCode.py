from DBcm import UseDatabase
import variables

dbconfig = {
    'host': '127.0.0.1',
    'user': variables.user_name,
    'password': variables.user_pass,
    'database': 'vsearchlogDB',
}

with UseDatabase(dbconfig) as cursor:
    _SQL ="""show tables"""
    cursor.execute(_SQL)
    data = cursor.fetchall()
    print(data)