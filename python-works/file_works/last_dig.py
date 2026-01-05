file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\numbers.txt"
fr=open(file_path,"r")
for line in fr:
    line=int(line.rstrip("\n"))
    dig=line%10
    print(dig)
