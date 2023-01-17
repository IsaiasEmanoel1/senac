import mysql.connector as mysql

def conn():
    mydb = mysql.connect(
        host = 'localhost',
        user = 'isaias',
        password = 'root',
        database = 'jegdii'
    )
    return mydb