def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact=fact*i
    return fact

fac={i:factorial(i) for i in range(1,11)}
print(fac)
