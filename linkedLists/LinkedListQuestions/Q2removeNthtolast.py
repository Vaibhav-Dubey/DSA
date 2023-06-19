import math


def search(nums, target):
    start, end = 0, len(nums)-1

        # Iterate when start index is less than end index
    while start < end:
        mid = math.floor((start + end) / 2)
        print(mid)
        # Target found so return immediately
        if target == nums[mid]:
            return mid
        # Target might be on the left side
        elif target < nums[mid]:
            end = mid - 1
        # Target might be on the right side
        else:
            start = mid + 1

    # When start and end index meet, return the index if it's the target
    if start == end and nums[start] == target:
        return start
    else:
        return -1


    
print(search([1,2,4,5,6],6))