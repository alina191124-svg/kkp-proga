A = [5, 8, 14, 11, 7, 3, 29, 8, 17, 74]
for i in range(10):
    for j in range(9-i):
        if A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
        print(A)
print(A)