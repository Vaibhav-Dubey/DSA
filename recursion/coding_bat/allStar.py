def allStar(s,index = 0):
    if index == len(s)-1:
        return s[index] 
    else:
        return s[index] + '*' + allStar(s,index+1)
print(allStar('hello',0)) 

def pairStar(s,index = 0):
    if index == len(s)-1:
        return s[index] 
    if s[index] == s[index+1]:
        return s[index] + '*' + pairStar(s,index+1)
    else:
        return s[index] + pairStar(s,index+1)
print(pairStar('hello',0)) 