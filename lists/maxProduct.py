#find max product of two integers in array where all elements are positive

def findMaxProd(arr1):
    maxprod = 1
    arr1.sort()
    for i in range(len(arr1)-1):
        if(arr1[i]*arr1[i+1] > maxprod):
            maxprod = arr1[i]*arr1[i+1]
    return maxprod

print(findMaxProd([1,20,30,44,5,56,8,9,10,31,58,57]))