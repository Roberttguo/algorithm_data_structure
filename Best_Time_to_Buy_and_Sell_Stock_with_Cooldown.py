'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one
share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
'''

#accepted on 10/21/2021
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mem = {}

        def helper(prices, day=0, purchased=False):
            if day >= len(prices):
                return 0
            if (day, purchased) in mem:
                return mem[(day, purchased)]

            if not purchased:
                buy = helper(prices, day + 1, not purchased) - prices[day]  # buy stock at day, able to buy next day
                not_buy = helper(prices, day + 1, purchased)  # wait for 1 day
                mem[(day, purchased)] = max(buy, not_buy)
            else:  # already bought
                sell = helper(prices, day + 2, not purchased) + prices[
                    day]  # if sell, have to wait 2 days to buy next time.
                not_sell = helper(prices, day + 1, purchased)
                mem[(day, purchased)] = max(sell, not_sell)
            return mem[(day, purchased)]

        return helper(prices, 0, False)
o=Solution()
prices = [1,2,3,0,2]
print (o.maxProfit(prices))