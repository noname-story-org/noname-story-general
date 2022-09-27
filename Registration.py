import pyodbc
import os

username = os.environ['USER_NAME']
password = os.environ['PASSWORD']

connection = pyodbc.connect('Driver={CData ODBC Driver for MySQL};' 'User=username;' 'Password=password;' 'Database=NonameStoryDB;' 'Server=localhost;' 'Port=3306;')
cursor = connection.cursor()

