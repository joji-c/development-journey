def square_list(*numbers):
    sqr=[]
    for n in numbers:
        sqr.append(n**2)
    return sqr

print(square_list(1,2,3,5,7))
