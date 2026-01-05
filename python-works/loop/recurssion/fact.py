def fact(num):
    if num==1:
        return 1
    return num * fact(num-1)

print(fact(5))

"""
fact(5) = 5 * fact(4)     5*24=120
fact(4) = 4 * fact(3)     4*6=24
fact(3) = 3 * fact(2)     3*2=6
fact(2) = 2 * fact(1)     2*1=2
fact(1) = 1
"""
