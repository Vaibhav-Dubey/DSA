def countX(s):  
    if s == "":
        return ""
    if s[0] == 'x':

        return  countX(s[1:])
    else:
        return s[0] + countX(s[1:])
print(countX('xxwpihizx'))