def array220(arr,index = 0):
    if index == len(arr) - 1:
        return False
    # if arr[index] == 20:
    #     return 1
    if arr[index] == 2 and arr[index+1] == 20:
            
            return True
    else: return array220(arr,index+1)
   
print(array220([11,20,2,20,9,0,11])) 