file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\years.txt"
fr=open(file_path,"r")


l=0
r=1
fib=0
fibi=[0,1]
while r<=3000:
    fib=l+r
    l=r
    r=fib
    fibi.append(fib)

lin=[]
for line in fr:
    line=int(line.rstrip("\n"))
    lin.append(line)

for i in lin:
    if i in fibi:
        print(i,end=" ")


    