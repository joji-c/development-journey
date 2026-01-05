from mysql import connector
class shop:
    def __init__(self):
        try:

            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                database="shop",
                use_pure=True
            )
            self.cursor= self.connection.cursor()
            print("db connected")
        except Exception as e:
            print(e)

    def add_product(self,**kwargs):
        try:
            columns=""
            values=""
            for k,v in kwargs.items():
                columns+=k+","
                values+="%s"+","
            columns=columns.rstrip(",")
            values=values.rstrip(",")

            query= f""" insert into cart ({columns}) values({values})"""
            data = [v for k,v in kwargs.items()]
            self.cursor.execute(query,data)
            self.connection.commit()
        except Exception as e:
            print(e)

    def list_products(self):
        query="select * from cart"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for row in records:
            print(row)

    def retrieve_product(self,id=None):
        query="select * from cart where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        print(record)

    def delete_product(self,id=None):
        query="delete from cart where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("row deleted")

    def update_product(self,id=None,**kwargs):
        place_holder=""
        for k,v in kwargs.items():
            place_holder=k+"="+"%s"+","
        place_holder=place_holder.rstrip(",")
        query=f""" update cart set {place_holder} where id={id}"""
        data=[v for k,v in kwargs.items()]
        self.cursor.execute(query,data)
        self.connection.commit()

product_instance=shop()
#product_instance.add_product(product_name="sugar",discount="no")
#product_instance.add_product(product_name="salt",discount="yes")

#product_instance.list_products()

#product_instance.retrieve_product(id=2)

#product_instance.delete_product(id=1)

#product_instance.update_product(product_name="paste",id=2)
#product_instance.retrieve_product(id=2)
