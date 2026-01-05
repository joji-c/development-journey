file_path="python-works\\file_works\\mental\\mental_health_social_media_dataset.csv"
fr=open(file_path,"r",encoding="utf-8")
import csv
read=csv.DictReader(fr)
data=[r for r in read]

#num of stressed users in each platform
str={}
for d in data:
    plat=d.get("platform")
    ment=d.get("mental_state")
    if ment == "Stressed":
        if plat in str:
            str[plat]+=1
        else:
            str[plat]=1
#print(str)

#num of users in each platform
p_percentage={}
for d in data:
    plat=d.get("platform")
    if plat in p_percentage:
        p_percentage[plat]+=1
    else:
        p_percentage[plat]=1
#print(p_percentage)

#most used platform
most_used=[k for k,v in p_percentage.items() if v==max(p_percentage.values())]
#print(most_used)

#percentage of stressed user per platform
stressed=list(str.values())
total=list(p_percentage.values())
keys=list(str.keys())
percentage=[]
for i in range(0,7):
    per=(stressed[i]/total[i])*100
    percentage.append(round(per,2))
plat_per=dict(zip(keys,percentage))
#print(plat_per)

#number of gender users
gender={}
for d in data:
    gen=d.get("gender")
    if gen in gender:
        gender[gen]+=1
    else:
        gender[gen]=1
#print(gender)

#percentage of peoples mental health
emo={}
for d in data:
    mood=d.get("mental_state")
    if mood in emo:
        emo[mood]+=1
    else:
        emo[mood]=1
for k,v in emo.items():
    v=round((v/len(data))*100,2)
    #print(k,v)

#age group in risk and average age that is at risk
risky_age={d.get("person_name"):int(d.get("age")) for d in data if d.get("mental_state")=="At_Risk"}
#print(risky_age)
sum=0
for k,v in risky_age.items():
    sum+=v
#print(f"Average at risk age: {round(sum/len(risky_age))}")


#healthy num of men ,women and others
gen_str=[d.get("gender") for d in data if d.get("mental_state")=="Healthy"]
#print(gen_str)
#print("count of healthy men:",gen_str.count("Male"))
#print("count of healthy women:",gen_str.count("Female"))
#print("count of healthy others:",gen_str.count("Other"))

#avg of pos and neg interactions
psum=0
pc=0
nsum=0
nc=0
for d in data:
    neg=int(d.get("negative_interactions_count"))
    pos=int(d.get("positive_interactions_count"))
    psum+=pos
    nsum+=neg
#print(f"Average positive interactions: {round(psum/len(data))}")
#print(f"Average negative interactions: {round(nsum/len(data))}")

#10 people with least sleep time
sleep={s.get("person_name"):float(s.get("sleep_hours")) for s in data}
least_sleep=sorted(sleep,key=lambda s:sleep.get(s))
#print(least_sleep[:10])