#  progressive sum of digits of a positive integer 

def digitSum(n):
    if n==0:
        return 0
    sum = n + digitSum(n-1)
    return sum 

print(digitSum(4))