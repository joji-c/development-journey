file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\words.txt"
fr=open(file_path,"r")
for line in fr:
    line=line.rstrip("\n")
    word=line.replace(" ","")
    if word==word[::-1]:
        print(word)
