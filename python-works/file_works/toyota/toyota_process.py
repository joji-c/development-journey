import csv
class CarPrice:
    def __init__(self):
        file_path="python-works\\object-oriented-programming\\inheritance\\toyota\\toyota.csv"
        fr=open(file_path,"r",encoding="utf-8")
        reader=csv.DictReader(fr)
        self.data=[r for r in reader]

    def avg_price(self):
        self.price=[int(d.get("price")) for d in self.data]
        print("Average price:",round(sum(self.price)/len(self.price)))

    def common_model(self):
        self.model=[d.get("model") for d in self.data]
        self.model_c={k:self.model.count(k) for k in self.model}
        self.max_model={k for k,v in self.model_c.items() if v==max(self.model_c.values())}
        print("common model:",self.max_model)

    def expensive_car(self):
        self.exp_car=[d.get("model") for d in self.data if int(d.get("price"))==max(int(d.get("price")) for d in self.data)]
        print(self.exp_car)

    def cheapest_car(self):
        self.ch_car=[d.get("model") for d in self.data if int(d.get("price"))==min(int(d.get("price")) for d in self.data)]
        print(self.ch_car)

    def avg_milage(self):
        self.milage=[int(d.get("mileage")) for d in self.data]
        print("Average milage:",round(sum(self.milage)/len(self.milage)))

    def transmition_count(self):
        self.transmission=[d.get("transmission") for d in self.data]
        self.transmission_c={k:self.transmission.count(k) for k in self.transmission}
        print(self.transmission_c)

    def cars_in_each_year(self):
        self.year=[d.get("year") for d in self.data]
        self.year_c={k:self.year.count(k) for k in self.year}
        self.max_year={k:v for k,v in self.year_c.items() if v==max(self.year_c.values())}
        print("max car produce year:",self.max_year)

    def petrol_users(self):
        self.fuel_type=[d.get("fuelType") for d in self.data]
        self.fuel_type_c={d:self.fuel_type.count(d) for d in self.fuel_type}
        print(self.fuel_type_c)
        self.petrol=[f for f in self.fuel_type if f=="Petrol"]
        print("number of petroleum cars:",len(self.petrol))

    def avg_year_price(self):
        self.year=[int(d.get("year")) for d in self.data]
        self.price=[int(d.get("price")) for d in self.data]
        self.avg_yr_pr={}
        for i in range(0,len(self.price)):
            if self.year[i] in self.avg_yr_pr:
                self.avg_yr_pr[self.year[i]]+=self.price[i]
            else:
                self.avg_yr_pr[self.year[i]]=self.price[i]
        print(self.avg_yr_pr)
        self.max_avg_peice={k:v for k,v in self.avg_yr_pr.items() if v==max(self.avg_yr_pr.values())}
        print("Max avg yearly price:",self.max_avg_peice)

    def cheap_model(self):
        self.cheapest=sorted(self.data,key=lambda d:int(d.get("price")))
        self.model_ch=[s.get("model") for s in self.cheapest][:5]
        print(self.model_ch)


car_instance=CarPrice()
#car_instance.avg_price()
#car_instance.common_model()
#car_instance.expensive_car()
#car_instance.cheapest_car()
#car_instance.avg_milage()
#car_instance.transmition_count()
#car_instance.cars_in_each_year()
#car_instance.petrol_users()
#car_instance.cheap_model()
