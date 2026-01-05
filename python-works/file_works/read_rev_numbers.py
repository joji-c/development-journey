file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\numbers.txt"

fr=open(file_path,"r")
for line in fr:
    line=line.rstrip("\n")
    print(line[::-1])
