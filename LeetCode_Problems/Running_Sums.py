'''1480. Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

'''

def runningSum(nums):
    runningSum=[]
    summ=0
    for i in range(len(nums)):
        summ+=nums[i]
        runningSum.append(summ)
    return runningSum

print(runningSum([1,2,3,5]))