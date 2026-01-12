x=int(input())
a=list(map(int,input().split()))
l=0
r=len(a)-1
ind=-1
while r-l>1:
    m=(l+r)//2
    if a[m]==x:
        ind=m
        l=m
    elif a[m]<x:
        l=m
    else:
        r=m
if ind!=-1:
    print(ind+1)
else:
    print('NO')