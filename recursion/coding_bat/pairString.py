def countPairs(s,index = 0):
    if index == len(s)-2:
        return 0
    elif s[index] == s[index+2]:
        return 1+countPairs(s,index+1)
    else:
        return countPairs(s,index+1)
print(countPairs('axax'))