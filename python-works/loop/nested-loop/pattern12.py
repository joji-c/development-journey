"""
* * * * *
 * * * *
   * *
    *
    *
   * *
 * * * *
* * * * *
"""
for r in range(1,5):
    for s in range(1,r+1):
        print(" ",end="")
    for c in range(5-r):
        print("*",end=" ")
    print()

for r in range(5,9):
    for s in range(1,10-r):
        print(" ",end="")
    for c in range(5,r+1):
        print("*",end=" ")
    print()
