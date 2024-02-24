def maxProdSub(nums):
    res = max(nums)
    currMin , currMax = 1, 1
    for n in nums :
        if n==0:
            currMax = 1
            currMin = 1
            continue
        temp = n * currMax
        currMax = max(n*currMax , n*currMin , n)
        currMin = min(temp ,n*currMin , n)
        res = max(res , currMax)
    return res

print(maxProdSub([1,2,3,4]))