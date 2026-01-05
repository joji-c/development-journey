"""
match case:
a case used when multiple option make different dicisions ,lower version of if elif, 
as we cant add diff condition for each case instead the input that the user gives is used to differentiate cases
"""

option = int(input("eneter a number 1.tea , 2.coffee ,3.without : "))
match option:
    case 1:
        print("you choose tea")
    case 2:
        print("you choose coffee")
    case 3:
        print("you choose without")
    case _:          #here case _: is used to show the default case similar to else:
        print("Invalid input")
    