n=0
for i in range (len(n)):
    low=i
    for j in range(i+1,len(n)):
        if n[j]<n[low]:
            low=j
    n[i],n[low]=n[low],n[i]