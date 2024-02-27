def countingBits(n):
    offset = 1
    dp = [0] * (n+1)

    for i in range(1,n+1):
        if offset*2==i:
            offset = i
        dp[i] = 1+dp[i-offset]
    return dp

print(countingBits(3))