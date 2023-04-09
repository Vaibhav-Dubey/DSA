#find a program  to find all pairs of integers whose sum is equal to a given number 

def twoSum(arr1,t):
    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)-1):
            if(arr1[i] + arr1[j]==t):
                print(i,j)
            else:continue

    

print(twoSum([2,6,3,8,11],9))
