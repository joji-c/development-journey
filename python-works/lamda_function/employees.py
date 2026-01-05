employee=[
    ["sam",34000,3],
    ["tom",42000,4],
    ["man",54000,6],
    ["don",23400,5],
    ["ron",134000,7]
]

srt_exp=sorted(employee,key=lambda emp:emp[2])
print(srt_exp)

srt_sal=sorted(employee,key=lambda emp:emp[1])
print(srt_sal)
