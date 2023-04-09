# check if an element is unique in an array

def isUnique(arr1):
    arr2=[]
    for i in range(len(arr1)):
        if (arr1[i] not in arr2):
            arr2.append(arr1[i])
        else:
            print("duplicate detected",arr1[i])
            arr2.remove(arr1[i])
    return arr2

print(isUnique([1,2,3,4,5,6,67,1,2,3]))