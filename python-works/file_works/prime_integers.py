file_path="C:\\Users\\jojic\\OneDrive\\Desktop\\development-journey\\python-works\\file_works\\integers.txt"
fr=open(file_path,"r")


def is_prime(n):
    for i in range(2,n):
            if n%i==0:
                return False
            else:
                return True

for line in fr:
    line=int(line.rstrip("\n"))
    if is_prime(line):
         print(line)

fr.close()