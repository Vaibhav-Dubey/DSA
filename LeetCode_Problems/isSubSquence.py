### leetcode 392 , subsequence question 
##ccases 14/18 my solution 

def isSubsequence(s,t):
    map1={}
    for i in range(len(s)):
        if s[i] not in list(t):
            return False
        if(s[i] in list(t)): 
            ch1 = s[i]
            map1[ch1] = t.index(ch1)
    list1 = list(map1.values())  
    print(len(list1))
    print(len(s))
    for i in range(len(list1)-1):
        if len(list1) != len(s):
            return False
        elif list1[i]>list1[i+1]:
           return False
    return True
print(isSubsequence("aaaaaa","bbaaaa"))

##cases: alll simple solution

def isSubsequence(self, s: str, t: str) -> bool:
    i = 0  # pointer for s
    j = 0  # pointer for t
    while i < len(s) and j < len(t):
        if s[i] == t[j]:  # if the characters match, move the pointer for s
            i += 1
        j += 1  # move the pointer for t regardless
    return i == len(s)  # if i has reached the end of s, s is a subsequence of t, else not