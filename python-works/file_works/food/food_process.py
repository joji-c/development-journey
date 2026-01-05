file_path="python-works\\file_works\\food\\Food_Nutrition_Dataset.csv.xls"
fr=open(file_path,"r",encoding="utf-8")

import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
#print(data)

food_calo={d.get("food_name"):float(d.get("calories")) for d in data}
max_calo={k:v for k,v in food_calo.items() if v==max(food_calo.values())}
#print("maximum calories:",max_calo)
min_calo={k:v for k,v in food_calo.items() if v==min(food_calo.values())}
#print("minimum calories:",min_calo)

food_prot={d.get("food_name"):float(d.get("protein")) for d in data}
max_prot={k:v for k,v in food_prot.items() if v==max(food_prot.values())}
#print("maximum protien:",max_prot)
min_prot={k:v for k,v in food_prot.items() if v==min(food_prot.values())}
#print("minimum protien:",min_prot)

food_carb={d.get("food_name"):float(d.get("carbs")) for d in data}
max_carb={k:v for k,v in food_carb.items() if v==max(food_carb.values())}
#print("maximum carbs:",max_carb)
min_carb={k:v for k,v in food_carb.items() if v==min(food_carb.values())}
#print("minimum carbs:",min_carb)

food_fat={d.get("food_name"):float(d.get("fat")) for d in data}
max_fat={k:v for k,v in food_fat.items() if v==max(food_fat.values())}
#print("maximum fat:",max_fat)
min_fat={k:v for k,v in food_fat.items() if v==min(food_fat.values())}
#print("minimum fat:",min_fat)

food_iron={d.get("food_name"):float(d.get("iron").replace('',"0")) for d in data}
max_iron={k:v for k,v in food_iron.items() if v==max(food_iron.values())}
#print("maximum iron:",max_iron)
min_iron={k:v for k,v in food_iron.items() if v==min(food_iron.values())}
#print("minimum iron:",min_iron)

food_vitamin_c={d.get("food_name"):float(d.get("vitamin_c").replace('','0')) for d in data}
max_vitamin_c={k:v for k,v in food_vitamin_c.items() if v==max(food_vitamin_c.values())}
#print("maximum vitamin_c:",max_vitamin_c)
min_vitamin_c={k:v for k,v in food_vitamin_c.items() if v==min(food_vitamin_c.values())}
#print("minimum vitamin_c:",min_vitamin_c)

food_cato={d.get("food_name"):d.get("category") for d in data}
type={}
for k,v in food_cato.items():
    if v in type:
        type[v]+=1
    else:
        type[v]=1
#print(type) 


empty_entry=[d.get("food_name") for d in data if d.get("iron")=='' or d.get("vitamin_c")=='']
#print(empty_entry)

c_sum=0
avg_calo_above=[]
for k,v in food_calo.items():
    c_sum+=v
for k,v in food_calo.items():
    if v>=(c_sum/len(food_calo)):
        avg_calo_above.append(k)
#print(avg_calo_above)

other=[]
for k,v in food_cato.items():
    if "other" in v.casefold():
        other.append(k)
#print(other)

apple=[]
for d in data:
    name=d.get("food_name")
    if "apple" in name.casefold():
        apple.append(d)
sum_apple_cal=0
for a in apple:
    calo=float(d.get("calories"))
    sum_apple_cal+=calo
#print("sum of calo from apple food:",sum_apple_cal)

cooked=[]
for d in data:
    name=d.get("food_name")
    if "cooked" in name.casefold():
        cooked.append(name)
#print(len(cooked))

muscle_food=[]
pro_sum=0
fat_sum=0
for d in data:
    pro=float(d.get("protein"))
    fat=float(d.get("fat"))
    pro_sum+=pro
    fat_sum+=fat
avg_pro=round(pro_sum/len(data))
avg_fat=round(fat_sum/len(data))
for d in data:
    name=d.get("food_name")
    pro=float(d.get("protein"))
    fat=float(d.get("fat"))
    if pro>avg_pro and fat<avg_fat:
        muscle_food.append(name)
print(muscle_food)
