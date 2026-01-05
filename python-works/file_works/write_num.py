file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\numbers.txt"
fw=open(file_path,"w")
for i in range(1,101):
    fw.write(str(i)+"\n")