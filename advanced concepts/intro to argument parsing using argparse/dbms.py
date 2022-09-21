import mysql.connector
from mysql.connector import Error

try: 
    connection = mysql.connector.connect(host='localhost', database='Assignment', user='dharaneesh', password='Dharaneesh@264')
    if connection.is_connected():
        df_info = connection.get_server_info()
        print('connected to mysql server version ', db_info)
        cursor = connection.cursor()
        cursor.execute('select database();')
        record = cursor.fetchone()
        print("You're conneted to database: ", record)
        
        
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection is closed')