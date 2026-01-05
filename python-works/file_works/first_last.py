file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\names.txt"
fr=open(file_path,"r")
for line in fr:
    line=line.rstrip("\n")
    print(line[0],line[-1])
