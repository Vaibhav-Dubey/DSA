# list operations 

##concatenation + operator

a= [1,2,3,4]
b=[1,2,3,5]
print(a+b)  #concatenates the two lists 
## * operation
c=[0]
print(c*4)

## len() function counts the number of integers in the list 

d=[1,2,3,4]
print(len(d))

## max / min function to return max in the list 

e=[1,2,3,5]
print(max(e),min(e))

## sum function to find some of elements in the list 
print(sum(e))

## conversion of string to list 
s= "vaibhav"
f=list(s)
print(f)

t= 'my name is vaibhav'
g=t.split()
h=list(t)
print(g,h) #will convert the string to list of words and not letters

##convert list back to string
print(' '.join(g))

