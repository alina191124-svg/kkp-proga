N=int(input())
A=list(map(int, input().split()))
maxx= A[0]
for i in range(1,N):
    if A[i]>maxx:
        maxx=A[i]
count=0
for i in range(N):
    if A[i]==maxx:
        count+=1
print(maxx, count)