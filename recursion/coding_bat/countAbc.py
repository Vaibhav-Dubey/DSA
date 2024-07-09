def countabc(s,index=0):
    if index >= len(s)-2:
        return 0 
    elif s[index:index+3] == 'abc':
        return 1+ countabc(s,index+3)

    elif s[index:index+3] == 'aba':
        return 1+countabc(s,index+2)
    else:
        return countabc(s,index+1)
print(countabc('abcxxabcxxaba'))