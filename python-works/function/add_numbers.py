#make a function to add two numbers
def add_numbers(num1,num2):
    result = num1+num2
    print(result)

add_numbers(120,220)
#a function with argument but no return



#make a fuction that returns  even or odd
def num_chk(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

print(num_chk(16)) #return give the value back with should either be stored in a variable or wrapped in print
#this is a function with argument and return