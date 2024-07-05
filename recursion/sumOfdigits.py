def sumOfDigits(n):
    print(n//10)
    if n==0:
        return 0
    return n%10 + sumOfDigits(n//10)
print(sumOfDigits(126))