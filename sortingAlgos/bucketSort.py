import math

def insertionSort(customList):
    for i in range(1,len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key<customList[j]:
            customList[j+1] = customList[j]
            j-=1
        customList[j+1] = key
    return customList

def bucketSort(cList):
    numberOfBuckets = round(math.sqrt(len(cList)))
    arr = []
    maxV= max(cList)
    for i in range(numberOfBuckets):
        arr.append([])
    for j in cList:
        index_b = math.ceil((j*numberOfBuckets)/maxV)
        arr[index_b-1].append(j)
    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])
    k=0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            cList[k]= arr[i][j]
            k+=1
    return cList

