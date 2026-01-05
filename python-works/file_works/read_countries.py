

file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\countries.txt"

fr=open(file_path,"r")

for line in fr:
    print(line,end="") #here we give no space or new line in print as the .txt file is made with all the necessary spaces
