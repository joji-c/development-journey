def sum_of_n(limit):
    if limit==1:
        return 1
    return limit + sum_of_n(limit-1)

print(sum_of_n(5))


"""
here all the recursions wait until the limit 1 is taken
sum_of_n(5) = 5 + sum_of_n(4)     5+10=15
sum_of_n(4) = 4 + sum_of_n(3)     4+6=10
sum_of_n(3) = 3 + sum_of_n(2)     3+3=6
sum_of_n(2) = 2 + sum_of_n(1)     2+1=3
sum_of_n(1) = 1

it works like this as all of these are saved in stacks
"""
