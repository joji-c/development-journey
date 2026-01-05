"""

lambda = anonymous function with a single expression

syntax:
lambda parameter: single expression

"""

add_num=lambda n1,n2:n1+n2
print(add_num(29,31))

square=lambda n:n**2
print(square(5))

cube=lambda n:n**3
print(cube(7))

odd_even=lambda n:"odd" if n%2!=0 else "even"
print(odd_even(13))

is_neg=lambda n:True if n<0 else False
print(is_neg(-11))

is_centuary_year=lambda n:True if n%100==0 else False
print(is_centuary_year(1230))

