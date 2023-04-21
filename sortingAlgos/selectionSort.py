def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for i in range(i+1,len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] =  customList[min_index],customList[i],
    return customList

