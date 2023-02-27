'''
Given a array of numbers representing the stock prices of a company in chronological order, write a function
that calculates the maximum profit you could have made from buying and selling that stock once. You must buy
before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars
and sell it at 10 dollars.
'''

#Pay attention to one-time allowance for stcok sale.

def maxProfit(prices):
    if len(prices)<2:
        return 0
    lowest_price=prices[0]
    running_max=0
    for i in range(1, len(prices)):
        running_max=max(running_max, prices[i]-lowest_price)
        lowest_price=min(lowest_price, prices[i])
    return running_max

prices=[9, 11, 8, 5, 7, 10]
print maxProfit(prices)

prices=[3,9, 11, 8,1, 5, 7, 10,20]
print maxProfit(prices)
