import pyodbc
import os

username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')

connection = pyodbc.connect('Driver={SQL Server};' 'Server=noname-story.com;' 'Database=NonameStoryDB;' 'UID=username;' 'PWD=password;')
cursor = connection.cursor()
cursor.execute()
