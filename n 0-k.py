N,K=map(int,input().split())
s=['']*N
def gen(n):
    if n==N:
        print(''.join(s))
        return
    for i in range(K):
        s[n]=str(i)
        gen(n+1)
gen(0)
