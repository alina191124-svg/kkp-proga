with open('17-1.txt','r') as f:
    nums=f.read().split()
    n=[int(x) for x in nums]
k=0
s=0
for i in range(len(n)-1):
    summ=n[i]+n[i+1]
    if (n[i]%10==7 or n[i+1]%10==7) and summ%12==0:
        k+=1
        if s<summ:
            s=summ
print(k,s)  



with open('','w') as f:
    f.write('\n')