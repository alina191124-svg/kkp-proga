with open('17-1.txt') as f:
    n=f.read().split()
s=0
for i in range(len(n)):
    nn=[int(x) for x in n[i]]
    if (s+min(nn))%7!=0:
        s+=min(nn)
    else:
        for j in range(2):
            if (s+nn[j])%7!=0 and (s+nn[j+1])%7!=0 and nn[j]<nn[j+1]:
                s+=nn[j]
            else:
                s+=nn[j+1]

print(s)