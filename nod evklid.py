def e(x,y):
    if y==0:
        return x
    print(x,y)
    return e(y,x%y)
print(e(48,18))

