"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # since the prices list is always non empty we always buy on the first day
        buy = prices[0]
        # we always start profit at 0
        profit = 0
        # loop through the array
        for n in prices:
            # if at any point we run into the smallest number in the array we change our buy value to that
            if n < buy:
                buy = n
            # then if we ever find a value greater than our buy we can calculate the max profit with the previous profit and the difference out the current price - our buy
            # note that we don't change the value of the buy in this case because we still want the smallest buy value to maximize our profit
            if n > buy:
                profit = max(profit, n - buy)
        # once we've gone through the list return the profit
        return profit
