"""
* * * * *
 *     *
   * *
    *
"""

for r in range(1,5):
    for c in range(1,8):
        if r==1 or r+c==8 or c-r==0:#here all the col in r4 is *
            print("*",end="")   #then all left side has a sum of 5 and all right side has a diff of 3
        else:
            print(" ",end="")
    print()