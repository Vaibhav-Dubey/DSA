#clear a dictionary

myDict={"one":1,"two":2}
myDict.clear()
print(myDict)

# copy a dictionary
myDict1={"one":1,"two":2}
mydict2=myDict1.copy()
print(mydict2)

# fromKeys method

newDict={}.fromkeys([1,2,3],0)   #creates a newDict with keys in the array seq and with values assigned in the next parameter 
print(newDict)

#get method 
myDict1.get("one",1)

#items method 

print(mydict2.items())

# keys method 
print(myDict1.keys())

#popitem method
print(mydict2.popitem())

#values meethod 
print(myDict1.values())

#update method 
mydict2.update(myDict1)

