#求最大公约数

def gcd(a,b):
    mi = min(a,b)
    ma = max(a,b)
    if ma%mi == 0:
        return mi
    return gcd(mi,(ma%mi))

print(gcd(12,2))