employee=[
    {"id":123,"name":"jack","email":"jck@gmail.com","salary":12000,"department":"hr"},
    {"id":234,"name":"jill","email":"jll@gmail.com","salary":23000,"department":"hr"},
    {"id":345,"name":"mark","email":"mrk@gmail.com","salary":34000,"department":"management"},
    {"id":456,"name":"pete","email":"pte@gmail.com","salary":45000,"department":"peoples"},
    {"id":567,"name":"rock","email":"rck@gmail.com","salary":56000,"department":"sales"}
]
all_names=[e.get("name") for e in employee]
print(all_names)

all_dep={em.get("department") for em in employee}
print(all_dep)

hr_names=[emp.get("name") for emp in employee if emp.get("department")=="hr"]
print(hr_names)

rich_names=[emp.get("name") for emp in employee if emp.get("salary")>30000]
print(rich_names)

dep_count={}
for e in employee:
    dep=e.get("department")
    if dep in dep_count:
        dep_count[dep]+=1
    else:
        dep_count[dep]=1
print(dep_count)