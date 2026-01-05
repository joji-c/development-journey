file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\years.txt"
fw=open(file_path,"w")
for year in range(1000,3000):
    fw.write(str(year)+"\n")
