import pyodbc
import os
import cgi, cgitb
import datetime
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
user_email = form.getvalue('user_email')

#Retrieves how many instances of the inputted username exists (if any) so that we know if we should tell the user to post a new  username
user_query = "SELECT COUNT(*) FROM userData WHERE userName = " + str(user_name) + ";"
userName_Count = int(cursor.execute(user_query))

#Creates the next available userID
user_id_query = "SELECT MAX(userID) FROM userData;"
user_id = int(cursor.execute(user_id_query)) + 1

#Gets the current date/time so that we can input the joinDate and initial loginDate
datetime_object = datetime.datetime.now()

#Checks to see if retrieved information is already in database (Also checks if DB is empty)
if(userName_Count > 0) : 
    #Throw error and reset if User is already in database
    
else : 
    #If user is not in database, insert new user data with an ID num equal to max + 1
