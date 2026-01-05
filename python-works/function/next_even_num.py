#find the next even number
def next_even(num):
    if num%2==0:
        return num+2
    else:
        return num+1



print(next_even(10))
print(next_even(9))