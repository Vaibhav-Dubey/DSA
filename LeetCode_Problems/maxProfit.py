'''
121 . You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
## o(n2) time complexity
# def maxProfit(prices):
#     n=len(prices)
#     if n == 0 or n== 1:
#         return 0
#     prof = 0 
#     for i in range(n-1):
#         for j in range(i+1,n):
#             maxi = prices[j] - prices[i]
#             if maxi > prof:
#                 prof = maxi
#     return prof



from cmath import inf


def maxProfit(prices):
    minprice= float(inf)
    maxprof=0
    for i in range(len(prices)):
        if(prices[i]<minprice):
            minprice=prices[i]
        elif(prices[i]-minprice>maxprof):
            maxprof = prices[i] - minprice
    return maxprof





print(maxProfit([2,1,2,1,0,1,2]))

