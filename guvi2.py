#Write a Python code to configure the MySQL Connector in your system and Insert data to MySQL Table after which you Fetch and Display data from Table
import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="12pswd",
database="contacts"
)

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE names")

s=(input()).split(" ")
for x in s:
	mycursor.execute("INSERT INTO names (ContactName)
VALUES (x)")

mycursor.execute("SELECT * FROM names")
namelist=mycursor.fetchall()
for x in namelist:
	print(x)