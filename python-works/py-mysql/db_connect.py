from mysql import connector
#first create a connection object
connection = connector.connect(
host="localhost",
user="root",
password="Password@123",
database="tripwisedb")

print("connection success")

connection.close()