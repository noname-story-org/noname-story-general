import pyodbc
import os
import cgi, cgitb
from io import StringIO

#Opens cgi.FieldStorage()
form = cgi.FieldStorage()

#Imports credentials from environment variables
username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')

#Query text templates
checkIsEmpty = "if exists(select * from userData)"

#Establishes a connection to the database
connection = pyodbc.connect('Driver={SQL Server};' 'Server=localhost;' 'Database=NonameStoryDB;' 'UID=username;' 'PWD=password;')
cursor = connection.cursor()

#Test if database connection works
#cursor.execute('SELECT * FROM userData')

#Retrieves information from Registration page
user_name = form.getvalue('user_name')
user_password = form.getvalue('user_password')

user_query = "SELECT COUNT(*) FROM userData WHERE userName = " + str(user_name) + ";"
userName_Count = cursor.execute(user_query)

#Checks to see if retrieved information is already in database (Also checks if DB is empty)
if(userName_Count > 0) : 
    
else : 
    
    #Throw error and reset if User is already in database
    #If user is not in database, insert new user data with an ID num equal to max + 1