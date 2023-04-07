from array import * 

## 1. Create an array and traverse 
arr1 = array('i',[1,2,3,4,5])

for i in arr1:
    print(i)     

## 2. Access Individual elements through indexes
print("Step 2")
print(arr1[0])

## 3. Append any value to array using append method 
print("step 3")

arr1.append(6)

print(arr1)

## 4. Insert value in an array using insert method 

print("step 4")
arr1.insert(1,7)
print(arr1)
## 5. Extend Python Array using extend method 
print("step 5")

arr2 = array('i',[10,11,12])
arr1.extend(arr2)
print(arr1)
## 6. Add items from list into array using fromlist() method
print("Step 6")
templist = [1,2,3]

arr1.fromlist(templist)
print(arr1)
## 7. remove any array element using remove method
print("step 7")
arr1.remove(12)
print(arr1)
## 8. remove last array element using pop 
print("step 8")
arr1.pop()
print(arr1)
## 9. Fetch any element through its index using index method 
print("step 9")
arr1.index(2)
print(arr1.index(2))
## 10. reverse a python array using reverse method 
print("step 10")
arr1.reverse()
print(arr1)
## 11. get array buffer information through buffer_info method
print("step 11")

print(arr1.buffer_info())
## 12. check for number of occurences of a number using count method 
print("step 12")

print(arr1.count(11))
## 13. convert array to python list 
# print("step 13")
# print(arr1.tolist())


## 14. slice elements form array 
print("step 14")
print(arr1[1:4])