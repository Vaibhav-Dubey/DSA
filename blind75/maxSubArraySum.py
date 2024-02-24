def MaxSubaraySum(nums):
    maxSubSum = nums[0]
    currSum = 0

    for n in nums:
        if currSum < 0:
            currSum = 0
        currSum +=n
        maxSubSum = max(maxSubSum,currSum)
    return maxSubSum


print(MaxSubaraySum([-1,4,1,2]))