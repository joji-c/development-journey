file_path="python-works\\file_works\\titanic\\titanic_dataset.csv"
fr=open(file_path,"r")

import csv
reader=csv.DictReader(fr)

data=[row for row in reader]
#print(data)

all_name=[dict.get("Name") for dict in data]
#print(all_name)

pass_cont=len(data)
#print("number of passengers:",pass_cont)

genders=[gen.get("Sex") for gen in data]
#print("male count:",genders.count("male"))
#print("female count:",genders.count("female"))

surv=[sur.get("Survived") for sur in data]
#print("survived",surv.count("1"))
#print("didn't survive",surv.count("0"))

pclass=[pc.get("Pclass") for pc in data]
#print("class 1:",pclass.count("1"))
#print("class 2:",pclass.count("2"))
#print("class 3:",pclass.count("3"))

yo=[int(y.get("Age")) for y in data if y.get("Age").isdigit()]
oldest_age=max(yo)
youngest_age=min(yo)
oldest=[ (p.get("Name") , p.get("Age")) for p in data if p.get("Age").isdigit and p.get("Age")==youngest_age]
#print(oldest)

first_ten=data[:11]
fir_ten=[p.get("Name") for p in first_ten]
#print(fir_ten)

port=[d.get("Embarked") for d in data if len(d.get("Embarked"))>0]
all_stat={p:port.count(p) for p in port }
#print(all_stat)

passeng=[d for d in data if d.get("Age").isdigit() and int(d.get("Age")) < 10]
#print(len(passeng))

survived=[p.get("Name") for p in passeng if p.get("Survived")=="1"]
#print(survived)
#print(len(survived))
unsurv=[d for d in data if d.get("Survived")=="0"]
surv=[d for d in data if d.get("Survived")=="1"]
unsur_per=(len(unsurv)/len(data))*100
sur_per=(len(surv)/len(data))*100
#print(round(unsur_per,2))
#print(round(sur_per,2))

male=[d for d in data if d.get("Sex")=="male"]
female=[d for d in data if d.get("Sex")=="female"]
sur_m=[m for m in male if m.get("Survived")=="1"]
sur_f=[f for f in female if f.get("Survived")=="1"]
m_per=(len(sur_m)/len(male))*100
f_per=(len(sur_f)/len(female))*100
#print(round(m_per,2))
#print(round(f_per,2))

fir_class=[d for d in data if d.get("Pclass")=="1"]
fir_sur=[f for f in fir_class if f.get("Survived")=="1"]
fir_per=(len(fir_sur)/len(fir_class))*100
print(round(fir_per,2))

sec_class=[d for d in data if d.get("Pclass")=="2"]
sec_sur=[s for s in sec_class if s.get("Survived")=="1"]
sec_per=(len(sec_sur)/len(sec_class))*100
print(round(sec_per,2))

thi_class=[d for d in data if d.get("Pclass")=="3"]
thi_sur=[t for t in thi_class if t.get("Survived")=="1"]
thi_per=(len(thi_sur)/len(thi_class))*100
print(round(thi_per,2))

