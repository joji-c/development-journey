py_path="python-works\\file_works\\python-basic\\python.csv"
pyt="python-works\\file_works\\python-basic\\python_batch.csv"
datasci="python-works\\file_works\\python-basic\\datascience_batch.csv"
rank_path="python-works\\file_works\\python-basic\\rank_list.csv"
attend_path="python-works\\file_works\\python-basic\\attendance_report.csv"
perf_path="python-works\\file_works\\python-basic\\performance_category.csv"

fr=open(py_path,"r")

"""for line in fr:
    line=line.rstrip("\n")
    print(line)"""

import csv
read=csv.DictReader(fr)
data=[row for row in read]
#print(data)

count_stud=len(data)
#print("total number of students is:",count_stud)

name_only=[d.get("NAME") for d in data]
#print(name_only)

student_batch={d.get("NAME"):d.get("BATCH") for d in data}
python_only={k:v for k,v in student_batch.items() if v=="Python"}
#print(python_only)

student_attendance={d.get("NAME"):float(d.get("PRESENT_%")) for d in data}
full_attendance={k:v for k,v in student_attendance.items() if v==100}
#print(full_attendance)

student_mcq={d.get("NAME"):d.get("MCQ1") for d in data}
#print(student_mcq)

student_overall={d.get("NAME"):float(d.get("OVERALL").replace("-","0")) for d in data}
max_overall=max(student_overall.values())
max_stud={k:v for k,v in student_overall.items() if v==max_overall}
#print(max_stud)

bel_30_stud={k:v for k,v in student_overall.items() if v<=30}
#print(bel_30_stud)

student_all={d.get("NAME"):d.get("OVERALL") for d in data}
null_stud={k:v for k,v in student_all.items() if v == '-'}
#print(null_stud)

"""new_stud="shadow,12.34,5,9.83,19,23,1,48,0,11,35.5,20,64.5,Python"
fw=open(py_path,"a")
fw.write(new_stud)
print(data)"""

py_count=0
ds_count=0
for d in data:
    bat=d.get("BATCH")
    if bat=="Python":
        py_count+=1
    elif bat=="Data Science":
        ds_count+=1
#print("Python student count:",py_count)
#print("Data science student count:",ds_count)

stud_above_20=[d for d in data if float(d.get("ABSENT_%"))>20]
#print(stud_above_20)

over=sorted(data,key=lambda k:float(k.get("OVERALL").replace("-","0")),reverse=True)
#print(over)

"""pb=open(pyt,"w")
for d in data: 
    if d.get("BATCH")=="Python":
        pb.write(str(d)+"\n")

das=open(datasci,"w")       
for d in data:
    if d.get("BATCH")=="Data Science":
        das.write(str(d)+"\n")"""


"""rl=open(rank_path,"w")
count=0
for d in over:
    count+=1
    d["Rank"]=count
    rl.write(str(d)+"\n")"""


p_batch=[d for d in data if d.get("BATCH")=="Python"]
sum_p=0
for line in p_batch:
    mcq_p=float(line.get("MCQ_XOBIN").replace("-","0"))
    sum_p+=mcq_p
avg_p=sum_p/len(p_batch)
#print("python class avg:",round(avg_p,2))

ds_batch=[d for d in data if d.get("BATCH")=="Data Science"]
sum_ds=0
for line in ds_batch:
    mcq_ds=float(line.get("MCQ_XOBIN").replace("-","0"))
    sum_ds+=mcq_ds
avg_ds=sum_ds/len(ds_batch)
#print("Data science class avg:",round(avg_ds,2))

sum=0
for line in data:
    mcq=float(line.get("MCQ_XOBIN").replace("-","0"))
    sum+=mcq
avg=sum/len(data)
#print("total avg:",round(avg,2))


"""ar=open(attend_path,"w")
for d in data:
    name=d.get("NAME")
    pres=d.get("PRESENT_COUNT")
    abs=d.get("ABSENT_COUNT")
    pres_per=d.get("PRESENT_%")
    ar.write(str(name)+" "+str(pres)+" "+str(abs)+" "+str(pres_per)+"\n")"""

pc=open(perf_path,"w")
for d in data:
    name=d.get("NAME")
    over=float(d.get("OVERALL").replace("-","0"))
    if over>=70:
        d["CATEGORY"]="Excellent"
    elif over>=40 and over<=69:
        d["CATEGORY"]="Good"
    elif over>=0 and over<=39:
        d["CATEGORY"]="Needs Improvement"

for d in data:
    pc.write(str(d)+"\n")