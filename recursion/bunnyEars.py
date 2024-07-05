def bunnyears(n):
    if n==0:
        return 0
    elif n%2==0:
        return 3+bunnyears(n-1)
    else: 
        return 2+bunnyears(n-1)
    
    
print(bunnyears(5))