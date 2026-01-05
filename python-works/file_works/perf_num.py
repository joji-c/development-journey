file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\numbers.txt"
fr=open(file_path,"r")

def is_perfect_number(number):
    sum=0
    num_cpy=number
    for i in range(1,number):
        if number%i==0:
            sum=sum+i
        if sum==num_cpy:
            return sum
        
per=[]
for line in fr:
    line=int(line.rstrip("\n"))
    if is_perfect_number(line):
        per.append(line)

print(per)
    