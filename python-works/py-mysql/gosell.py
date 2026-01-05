from mysql import connector
class vehicle:
    def __init__(self):
        try:

            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                database="gosell_db",
                use_pure=True
            )
            self.cursor= self.connection.cursor()
            print("db connected")
        except Exception as e:
            print(e)

    def add_vehicle(self,**kwargs):
        try:
            columns=""
            values=""
            for k,v in kwargs.items():
                columns+=k+","
                values+="%s"+","
            columns=columns.rstrip(",")
            values=values.rstrip(",")

            query= f""" insert into vehicle ({columns}) values({values})"""
            data = [v for k,v in kwargs.items()]
            self.cursor.execute(query,data)
            self.connection.commit()
        except Exception as e:
            print(e)

# vehicle_instance=vehicle()
# vehicle_instance.add_vehicle(name="splendor",price=20000,year=2010,fuel_type="petrol",comments="good condition",running_km=1000,owner_type="single",owner="jibin",location="kakkanad")
# vehicle_instance.add_vehicle(name="yamaha",price=30000,year=2015,fuel_type="petrol",comments="good condition",running_km=1000,owner_type="single",owner="sibin",location="kakkanad")
# print("data inserted")

    def list_vehicle(self):
        query="select * from vehicle"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for row in records:
            print(row)
# vehicle_instance=vehicle()
# vehicle_instance.list_vehicle()

    def retrieve_vehicle(self,id=None):
        query="select * from vehicle where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        print(record)
# vehicle_instance=vehicle()
# vehicle_instance.retrieve_vehicle(id=2)
    def delete_vehicle(self,id=None):
        query="delete from vehicle where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("row deleted")
# vehicle_instance=vehicle()
# vehicle_instance.delete_vehicle(id=1)
    def update_vehicle(self,id=None,**kwargs):
        place_holder=""
        for k,v in kwargs.items():
            place_holder=k+"="+"%s"+","
        place_holder=place_holder.rstrip(",")
        query=f""" update vehicle set {place_holder} where id={id}"""
        data=[v for k,v in kwargs.items()]
        self.cursor.execute(query,data)
        self.connection.commit()
#vehicle_instance=vehicle()
#vehicle_instance.update_vehicle(name="hayabusa",id=2)
#vehicle_instance.retrieve_vehicle(id=2)
