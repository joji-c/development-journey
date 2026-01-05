numbers=[150,151,153,148,153,1634,1700,1634,153]
def is_armstrong(num):
    num_cpy=num
    total=0
    count=len(str(num))
    while num!=0:
        digit=num%10
        exp=digit**count
        total+=exp
        num=num//10
    if num_cpy==total:
        return True

armstrong={num:numbers.count(num) for num in numbers if is_armstrong}
count={k for k,v in armstrong.items() if v>1}
print(count)
