# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low, profit = 10000, 0
        for i in range( len( prices ) ):
            if prices[ i ] < low:
                low = prices[ i ]
            elif profit < prices[ i ] - low:
                profit = prices[ i ] - low
        return profit
