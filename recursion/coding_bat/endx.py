def endX(s, index = 0,count=0):
    if index == len(s)-1:
        return 'x'*count
    if s[index] == 'x':
        return endX(s,index+1,count+1)
    else:
        return s[index] + endX(s,index+1,count) 
print(endX('axxaaxx'))