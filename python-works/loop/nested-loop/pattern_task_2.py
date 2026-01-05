for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print("R",end=" ")
        
        else:
            print("S",end=" ")
    print()