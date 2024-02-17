#Given a word and a text, return the count of occurrences of the anagrams of the word in the text.

# For eg. word is “for” and the text is “forxxorfxdofr”, then the program should return 3 as output.

#text = gotxxotgxdogt, word = got

from collections import defaultdict


# def countAnagram(s, p):
#     if (len(s) < len(p)):
#             return False
#         # counter = 0
#     res=[]
#     h=0
#     t=len(p)-1
#     p = list(p)
#     # print(p)
#     while(t<len(s)):
#         lookUp={}
#         for i in range(len(p)):
            
#             # print(s[i+h])
#             lookUp[s[i+h]] = i
#             if s[i+h] not in p and lookUp[s[i+h]] == :
#                 print(i+h)
#                 flag=0
#                 break
#             else:flag=1
#             print(lookUp)
#         print(res,flag) 
#         if flag==1:
#             res.append(h)
#         h+=1
#         t+=1

#     return res

# print(countAnagram('cbaebabacd', 'abc'))

def findAnagrams(s,p):
    hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
    if pL > sL: return []

    # build hashmap
    for ch in p: hm[ch] += 1
    print(hm)
    # initial full pass over the window
    for i in range(pL-1):
        if s[i] in hm: hm[s[i]] -= 1
        
    # slide the window with stride 1
    for i in range(-1, sL-pL+1):
        if i > -1 and s[i] in hm:
            hm[s[i]] += 1
        if i+pL < sL and s[i+pL] in hm: 
            hm[s[i+pL]] -= 1
            
        # check whether we encountered an anagram
        if all(v == 0 for v in hm.values()): 
            res.append(i+1)
            
    return res
print(findAnagrams('cbaebabacd', 'abc'))