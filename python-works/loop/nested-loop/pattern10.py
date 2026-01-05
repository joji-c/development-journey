"""   *
     * *
    *   *
   *     *
    *   *
     * *
      *
"""
for r in range(1,8):
    for c in range(1,8):
        if r+c==5 or c-r==3 or r-c==3 or r+c==11:
            print("*",end="") 
        else:
            print(" ",end="")
    print()
