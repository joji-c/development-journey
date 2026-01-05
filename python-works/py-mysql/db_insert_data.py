from mysql import connector

connection = connector.connect(
host="localhost",
user="root",
password="Password@123",
database="tripwisedb")

cursor=connection.cursor()

query="""
insert into user(name,email,password) values(%s,%s,%s)
"""

data = [("ana","ana@gmail.com","ana@123"),
        ("jacob","jacob@gmail.com","jacob@123"),
        ("jack","jack@gmail.com","jack@123"),
        ("cob","cob@gmail.com","cob@123")
        ]

cursor.executemany(query,data)
connection.commit()   #help create a savepoint
print ("insert success")

cursor.close()
connection.close()
