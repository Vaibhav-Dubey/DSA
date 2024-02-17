#Given an array of positive integers and a positive numberk, find the maximum sum of any contiguous subarray of size k.
def maxSubArraySum(arr,k):
    if(len(arr)<k):
        return False
    value = {}
    h = 0
    t = k-1
    while(t<=len(arr)):
        sums = 0
        for i in range(k):
            sums += arr[i]
            value[h] = sums
            h += 1
            t += 1
    # print(list(value.values()))
    return max(list(value.values()))

print(maxSubArraySum([3, 5, 2, 1, 7],2))