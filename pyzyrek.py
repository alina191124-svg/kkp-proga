a=[2,11,8,5,7,12,3,55,6,15]
s=0
for i in range(0,9):
    if a[i]<a[i+1]:
        a[i+1],a[i]=a[i],a[i+1]
        s+=a[i]
    print(s)