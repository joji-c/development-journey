"""
1
2 3
4 5 6
7 8 9 10
"""
count=0
for r in range(1,5):
    for c in range(1,r+1):
        count+=1
        print(count,end=" ")
    print()