from mysql import connector
connection=connector.Connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb"
)

cursor=connection.cursor()

query="select * from user where id=%s"
data=(1,)
cursor.execute(query,data)

records=cursor.fetchone()
print(records)

cursor.close()
connection.close()
