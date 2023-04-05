# Fibonacci is a sequence of numbers where each number is sum of preceeding two numbers and the sequence starts from 0 and 1 
# 0,1,1,2,3,5,8,13,21,34,55,89 ....
def fibo(n):
    assert n>=0 and int(n) ==n, 'The number must be non negative integer'  ### STEP 3 : The Constraint
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fiboNum = fibo(n-1)+fibo(n-2)
        return fiboNum
    
print(fibo(7))