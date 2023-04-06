# find greatest common divisor of two numbers 

# we use the euclidean algo here

def gcd(n,m):
    print(n,m)
    if m == 0:
        return n
    else:
        return gcd(m,n%m)

print(gcd(48,18))