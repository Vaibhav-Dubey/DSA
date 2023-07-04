def twoSum(nums, target):
    complementMap = dict()
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if num in complementMap:
            return[complementMap[num],i]
        else:
            complementMap[complement] = i


print(twoSum([3,2,4],6))