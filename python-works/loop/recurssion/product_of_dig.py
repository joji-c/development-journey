def prod(num):
    if num==0:
        return 1
    return num%10 * prod(num//10)

print(prod(543))

"""
prod(543) = 3 * prod(54)   3*20=60
prod(54) = 4 * prod(5)     4*5=20
prod(5) = 5 * prod(0)      5*1=5
prod(0) = 1
"""
