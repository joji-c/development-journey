"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
for r in range(1,6):
    for s in range(1,r):
        print(" ",end="")
    for c in range(1,7-r):
        print("*",end="") #add a space here to make the pattern inro a upside down triangle
    print()
