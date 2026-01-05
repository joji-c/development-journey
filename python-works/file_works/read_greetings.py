file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\greetings.txt"

fr=open(file_path,"r")
st=set()
for line in fr:
    st.add(line.rstrip("\n"))
print(st)


"""for line in set(fr):
    print(line,end="")"""
