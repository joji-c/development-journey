"""
   1
  1 1
 1 2 1
1 3 3 1
"""

for r in range(1,5):
    for s in range(1,5-r):
        print(" ",end="")
    for c in range(1,r+1):
        print(1,end=" ")
    print()

#not ciompleted
