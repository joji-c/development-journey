from mysql import connector
connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb"
)

cursor=connection.cursor()
query="update user set name=%s,password=%s where id = %s"
data=('anna','anna@123',1)
cursor.execute(query,data)
connection.commit()

cursor.close()
connection.close()
