student={"name":"joji","age":22,
         "grade":"b"}
count=0
print(student["name"])
student["school"]="city high school"
student["grade"]="a+"
student.pop("age")
student.get("name")
for s in student:
    count+=1
print("number of key value pair:",count)

for k in student.keys():
    print(k)

for v in student.values():
    print(v)
      
for k,v in student.items():
    print(k,v)
