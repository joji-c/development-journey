"""
decision making : taking actions based on the result of a condition

if-else
if condition:
    stat1
    stat2
else:
    stat3
    stat4

note: if there is more than two conditions use elif function to 
add more as we cannot add any function in else function.
if elif is used there is no need to add else in such cases if its not required.
"""

age = int(input("enter age: "))
if age>= 18:
    print("is eligible for voting")
else:
    print("is not eligible for voting")
