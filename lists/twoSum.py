#find a program  to find all pairs of integers whose sum is equal to a given number 

def twoSum(arr1,t):
    indexArr=[]
    mainIndex=[]
    arr2=arr1
    for i in range(len(arr1)):
        print(arr1[i])
        searchNum= (t - arr1[i])
        print("searchNum",searchNum)
        arr2.remove(arr2[i])
        print(arr2)
        if(searchNum in arr2):
            indexArr.append(i)
            indexArr.append(arr2.index(searchNum) + 1)
            mainIndex.append(indexArr)
        else:continue

    return mainIndex

print(twoSum([2,6,3,8,11],9))
