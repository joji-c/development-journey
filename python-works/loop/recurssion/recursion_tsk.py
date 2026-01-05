def print_numbers_ascending(n):
    if n == 0:
        return
    print_numbers_ascending(n - 1)
    print(n)
print_numbers_ascending(5)
print("===")

def sum_numbers(num):
    if num==0:
        return 0
    return num+sum_numbers(num-1)
print(sum_numbers(5))
print("===")

def fact_numbers(num):
    if num==1:
        return 1
    return num*fact_numbers(num-1)
print(fact_numbers(6))
print("===")

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))
print("===")

def num_of_digits(n):
    if n==0:
        return 0
    c=0
    d=n%10
    c+=1
    return c+num_of_digits(n//10)
print(num_of_digits(2287))
print("===")

def sum_digits(n):
    if n==0:
        return 0
    d=n%10
    return d+sum_digits(n//10)
print(sum_digits(227))
print("===")

def reverse_num(n):
    if n==0:
        return ""
    d=n%10
    return str(d)+str(reverse_num(n//10))
print(reverse_num(227))
print("===")

def power_of_num(num,pow):
    if pow==0:
        return 1
    return num*power_of_num(num,pow-1)
print(power_of_num(2,3))
print("===")
