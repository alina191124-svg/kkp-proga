n=0
for i in range(1,len(n)):
    it=n[i]
    j=i-1
    while j>0 and n[j]>it:
        n[j+1]=n[j]
        j-=1
    n[j+1]=it
