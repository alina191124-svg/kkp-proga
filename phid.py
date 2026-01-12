
def ph(n):
    if n==1 or n==2:
        return 1
    else:
        return ph(n-1)+ph(n-2)
n=int(input())
print(ph(n))