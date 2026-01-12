N=int(input())
mi=10000000000000000000000000000000000
ma=0
for i in range(N):
    n=int(input())
    if n%2==0 and n>0:
        if n<mi:
            mi=n 
        if n>ma:
            ma=n 
print(mi,ma)