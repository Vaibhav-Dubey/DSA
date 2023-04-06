# 54 sum of digit should be 9 

def sumOfDigit(n):
    if n==0:
        return 0
    else:
        sums= n%10 + sumOfDigit(n//10)
        return sums

print(sumOfDigit(544))