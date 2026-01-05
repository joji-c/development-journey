letters = ['A', 'B', 'C', 'D']
n = len(letters)

for i in range(n):
    for j in range(n):
        print(letters[(i + j) % n], end=' ')
    print()