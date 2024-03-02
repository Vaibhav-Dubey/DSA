# 70 clibimg stairs is a dynamic programming problem where in we try and find a bottom up problem solution to the problem and find a pattern 

def climStairs(n):
    one, two =1 , 1
    for i in range(n-1):
        temp = one 
        one = one + two 
        two = temp 

    return one 

print(climStairs(5))