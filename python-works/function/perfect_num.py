#if all the divisor of a num is added gives that number then it is a perfect number (except that num as a divisor)

def is_perfect_number(number):
    flag = True
    sum=0
    num_cpy=number
    for i in range(1,number):
        if number%i==0:
            sum=sum+i
        if sum==num_cpy:
            flag=True
        else:
            flag=False
    return flag


print(is_perfect_number(28))
print(is_perfect_number(27))
print(is_perfect_number(6))

