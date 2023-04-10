# given a 2-D list , one has to invert it 90 degrees and then preint the rotated list 

# rotated matrixx

mylist=[[1,2,3],[4,5,6],[7,8,9]]
print(mylist)
n=len(mylist)
print(n//2)

for layer in range(n//2):
    first = layer 
    last = n-layer-1
    print(layer)
    for i in range(first, last):
        print(i)
        top = mylist[layer][i] # initialise the top left element 
        #bottom left   to top left 
        mylist[layer][i] = mylist[-i-1][layer]
        #bottom right to bottom left 
        
        mylist[-i-1][layer] = mylist[-layer-1][-i-1]
        # move top right to bottom right 
        mylist[-layer-1][-i-1] = mylist[i][-layer-1]
        #move top left to top righ 
        mylist[i][-layer-1] = top
print(mylist)