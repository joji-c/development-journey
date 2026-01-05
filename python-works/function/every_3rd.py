string="ABCDEFGHIJKLMN"
for i in range(0,len(string)):
    if i==0 or i%3==0:
        print(string[i],end="")