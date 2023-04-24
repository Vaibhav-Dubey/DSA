def insertionSort(customList):
    for i in range(1,len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key<customList[j]:
            customList[j+1] = customList[j]
            j-=1
        customList[j+1] = key
    return customList
print(insertionSort([5,4,3,2,1]))