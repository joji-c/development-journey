vehicles = [
    {"name": "Swift", "brand": "Maruti Suzuki", "price": 650000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Baleno", "brand": "Maruti Suzuki", "price": 820000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Creta", "brand": "Hyundai", "price": 1500000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "i20", "brand": "Hyundai", "price": 950000, "model": 2021, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Seltos", "brand": "Kia", "price": 1600000, "model": 2023, "color": "Silver", "fuel_type": "Diesel"},
    {"name": "Sonet", "brand": "Kia", "price": 1200000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Harrier", "brand": "Tata", "price": 1900000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "Nexon", "brand": "Tata", "price": 1200000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Punch", "brand": "Tata", "price": 800000, "model": 2023, "color": "Green", "fuel_type": "Petrol"},
    {"name": "XUV700", "brand": "Mahindra", "price": 2200000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Thar", "brand": "Mahindra", "price": 1700000, "model": 2022, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Scorpio N", "brand": "Mahindra", "price": 2000000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "City", "brand": "Honda", "price": 1500000, "model": 2021, "color": "Silver", "fuel_type": "Petrol"},
    {"name": "Amaze", "brand": "Honda", "price": 900000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Kiger", "brand": "Renault", "price": 800000, "model": 2021, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Duster", "brand": "Renault", "price": 1300000, "model": 2020, "color": "Brown", "fuel_type": "Diesel"},
    {"name": "EcoSport", "brand": "Ford", "price": 1100000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Endeavour", "brand": "Ford", "price": 3600000, "model": 2020, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Altroz", "brand": "Tata", "price": 950000, "model": 2022, "color": "Golden", "fuel_type": "Petrol"},
    {"name": "Venue", "brand": "Hyundai", "price": 1300000, "model": 2023, "color": "Red", "fuel_type": "Petrol"}
]
print("-----1-----")
#cars names with red color
for v in vehicles:
    col=v.get("color")
    if col=="Red":
        print(v.get("name"))

print("-----2-----")
#car names for model 2022
for v in vehicles:
    mod=v.get("model")
    if mod==2022:
        print(v.get("name"))

print("-----3-----")
#car names for diesel types
for v in vehicles:
    fu=v.get("fuel_type")
    if fu=="Diesel":
        print(v.get("name"))

print("-----4-----")
#all car prices
price={}
for v in vehicles:
    name=v.get("name")
    pr=v.get("price")
    if name in price:
        price[name]+=pr
    else:
        price[name]=pr
print(price)

print("-----5-----")
#car name for price above 10lakh
for v in vehicles:
    pr=v.get("price")
    if pr>1000000:
        print(v.get("name"))

print("-----6-----")
#car with brand tata
for v in vehicles:
    br=v.get("brand")
    if br=="Tata":
        print(v.get("name"))

print("-----7-----")
#tata car with model 2022
for v in vehicles:
    br=v.get("brand")
    mod=v.get("model")
    if br=="Tata" and mod==2022:
        print(v.get("name"))

print("-----8-----")
#lowest price vehicle
low={}
for v in vehicles:
    pr=v.get("price")
    nam=v.get("name")
    if nam in low:
        low[nam]+=pr
    else:
        low[nam]=pr
min_pr=(min(low.values()))
print(min_pr)

print("-----9-----")
#price of maruthi suzuki
maru={}
for v in vehicles:
    pr=v.get("price")
    br=v.get("brand")
    nam=v.get("name")
    if br=="Maruti Suzuki":
        if br in maru:
            maru[nam]+=pr
        else:
            maru[nam]=pr
print(maru)

print("-----10-----")
#hundai vehic above 5 lakh
hund={}
for v in vehicles:
    pr=v.get("price")
    br=v.get("brand")
    nam=v.get("name")
    if br=="Hyundai" and pr>500000:
        if br in hund:
            hund[nam]+=pr
        else:
            hund[nam]=pr
print(hund)

print("-----11-----")
#car model btw 2022-2024
for v in vehicles:
    bnam=v.get("name")
    mod=v.get("model")
    if mod>=2022 and mod<=2024:
        print(v.get("name"))

print("-----12-----")
#which brand has more cars
num={}
for v in vehicles:
    br=v.get("brand")
    if br in num:
        num[br]+=1
    else:
        num[br]=1
print(num)
max_car_brand=max(num.values())
for k,v in num.items():
    if v==max_car_brand:
        print(k,v)

print("-----13-----")
#costly car in mahindra and tata
mah={}
tata={}
for v in vehicles:
    br=v.get("brand")
    pr=v.get("price")
    nam=v.get("name")
    if br=="Mahindra":
        if br in mah:
            mah[nam]+=pr
        else:
            mah[nam]=pr
    if br=="Tata":
        if br in tata:
            tata[nam]+=pr
        else:
            tata[nam]=pr

max_pr_mahindra=max(mah.values())
max_pr_tata=max(tata.values())

for k,v in mah.items():
    if v==max_pr_mahindra:
        print(k,v)
for k,v in tata.items():
    if v==max_pr_tata:
        print(k,v)

print("-----14-----")
#which model has more cars
model={}
for v in vehicles:
    mod=v.get("model")
    if mod in model:
        model[mod]+=1
    else:
        model[mod]=1
print(model)
max_car_model=max(model.values())
for k,v in model.items():
    if v==max_car_model:
        print(k,v)
        