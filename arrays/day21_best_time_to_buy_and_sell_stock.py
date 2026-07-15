"""
LeetCode 121: Best Time to Buy and Sell Stock

Approach:
- Keep track of the minimum price seen so far.
- Calculate the profit if selling today.
- Update the maximum profit.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
         
        for price in prices:
            if price < min_price:
              min_price = price
 
            profit = price - min_price


            if profit > max_profit :
                max_profit = profit 

        return max_profit        