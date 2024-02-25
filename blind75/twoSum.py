def twoSum(nums, target):
    prevMap={}
    for i , n in enumerate(nums):
        if target-n in prevMap:
           return [prevMap[target-n],i]
        prevMap[n] = i
return  


print(twoSum([3,2,4],6))