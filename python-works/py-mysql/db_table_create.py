from mysql import connector
#first create a connection object
connection = connector.connect(
host="localhost",
user="root",
password="Password@123",
database="tripwisedb")
#second create a cursor object
cursor=connection.cursor()

#write the queery in a variable
query="""
create table user(
    id int primary key auto_increment,
    name varchar(200) not null,
    email varchar(200) not null unique,
    password varchar(200) not null
);
"""
#execute the query using the variable
cursor.execute(query)
print("table created")

cursor.close()
connection.close()