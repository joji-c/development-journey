"""

*****
 *****
  *****
   *****
    *****
    
"""
for r in range(1,6):
    for s in range(1,r): #if we use 6-r instead of r it will turn right
        print(" ",end="")
    for c in range(1,6):
        print("*",end="")
    print()
