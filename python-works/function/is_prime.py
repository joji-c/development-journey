def is_prime(num):
    flag=True
    for i in range(2,num):
        if num%i==0:
            flag=False
            break
        else:
            flag=True
    return flag


print(is_prime(11))
print(is_prime(10))
print(is_prime(19))

