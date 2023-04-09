## need to find the missing number in an array of integers 1 to 100 
## given an array of 1 to 100 , need to find missing number 

def findMissingNumber(arr1):
    sumE = (100*101)//2
    sumA = sum(arr1)
    return (sumE - sumA)
arr1=[]

# to get the 100 elements in a list
for i in range(0,100):
    
    arr1.append(i+1)
print(arr1)

# remove any element required 
arr1.remove(23)
arr2 = arr1
print(findMissingNumber(arr2))