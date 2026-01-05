"""
         *
       * *
     * * *
   * * * *
 * * * * *
"""
for r in range(1,6):
    for s in range(1,6-r):
        print(" ",end="")
    for c in range(1,r+1):
        print("*",end="")  #add a space in the end gere to make the shape into a triangle
    print()
