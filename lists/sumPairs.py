def pairSum(myList, sum):
    pairSumList=[]
    myListDup = myList 
    for i in range(len(myList)):
        print(myList[i])
        num1 = (sum-myList[i])
        del myListDup[i]
        print(myListDup)
        # if(num1 in myListDup):
        #     str1 = str(i)+"+"+str(num1)
        #     pairSumList.append(str1)
        # else:continue
    return pairSumList

print(pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))