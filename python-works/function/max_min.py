#function to display the largest of two numbers
def max_two(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

 #function to display the smallest of two numbers   
def min_two(num1,num2):
    if num1<num2:
        return num1
    else:
        return num2

print(max_two(10,20))
print(min_two(10,20))
