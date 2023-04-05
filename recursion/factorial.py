# A program to calculate the factorial of a given number using recursion


def factorial(n):
    assert n>=0 and int(n) ==n, 'The number must be non negative integer'  ### STEP 3 : The Constraint
    if(n==0):  ### STEP 2: The stopping case
        return 1
    else:
        fact = n * factorial(n-1)  ### STEP 1: The recursive case
        return fact

print(factorial(-1))