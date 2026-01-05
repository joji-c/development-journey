file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\years.txt"
fr=open(file_path,"r")
leap=[]
for line in fr:
    line=line.rstrip("\n")
    line=int(line)
    if (line%100==0 and line%400==0) or (line%100!=0 and line%4==0):
        leap.append(line)
print(leap)