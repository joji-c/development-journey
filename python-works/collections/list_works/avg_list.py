def average_list(*numbers):
    sum=0
    for n in numbers:
        sum+=n
    avg=sum/len(numbers)
    return avg

print(average_list(1,2,3,4,5))
