def IsPrime(n, d=3):
    if d*d>n:
        return True
    if n%2==0:
        return False
    if n % d == 0:
        return False
    return IsPrime(n, d + 2)
a = int(input())
if IsPrime(a):
    print('YES')
else:
    print('NO')