file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\words.txt"
fr=open(file_path,"r")
for r in fr:
    r=r.rstrip("\n")
    word=r.replace(" ","")
    print(word)
