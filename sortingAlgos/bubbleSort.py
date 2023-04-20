def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            customList[j]>customList[j+1]
            customList[j],customList[j+1] = customList[j+1],customList[j]
    return customList

print(bubbleSort([5,4,3,2,1]))            
