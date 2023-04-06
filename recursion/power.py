# find the nth power of a number x 

def power(n,p):
    if p==0:
        return 1
    else:
        return n*power(n,p-1)
print(power(2,2))