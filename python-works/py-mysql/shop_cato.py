from mysql import connector
class category:
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

    def create_category(self):
        try:
            query=  """
                    create table category(
                    id int primary key auto_increment,
                    category_name varchar(200) not null);
                    """
            self.cursor.execute(query)
            self.connection.commit()
            print("table created")
        except Exception as e:
            print(e)

    def add_category(self,**kwargs):
        try:
            columns=""
            values=""
            for k,v in kwargs.items():
                columns+=k+","
                values+="%s"+","
            columns=columns.rstrip(",")
            values=values.rstrip(",")

            query= f""" insert into category ({columns}) values({values})"""
            data = [v for k,v in kwargs.items()]
            self.cursor.execute(query,data)
            self.connection.commit()
            print("records added")
        except Exception as e:
            print(e)

    def retrieve_category(self,id=None):
        query="select * from category where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        print(record)

    def delete_category(self,id=None):
        query="delete from category where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("record deleted")

    def update_category(self,id=None,**kwargs):
        place_holder=""
        for k,v in kwargs.items():
            place_holder=k+"="+"%s"+","
        place_holder=place_holder.rstrip(",")
        query=f"""update category set {place_holder} where id={id}"""
        data=[v for k,v in kwargs.items()]
        self.cursor.execute(query,data)
        self.connection.commit()

category_instance=category()
#category_instance.create_category()

#category_instance.add_category(category_name="toys")
#category_instance.add_category(category_name="cloths")

#category_instance.retrieve_category(id=2)

#category_instance.delete_category(id=1)

#category_instance.update_category(category_name="paste",id=2)
