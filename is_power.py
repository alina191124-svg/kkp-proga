def is_power(x):
    if x==1:
        return True
    if x%2==0:
        return is_power(x//2)
    return False