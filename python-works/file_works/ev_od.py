file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\numbers.txt"
fr=open(file_path,"r")
even=[]
odd=[]
for line in fr:
    line=int(line.rstrip("\n"))
    if line%2==0:
        even.append(line)
    else:
        odd.append(line)
print(even)
print(odd)