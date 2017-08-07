# -*- coding:utf-8 -*-

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
	def maxProfit(self, prices):
		"""
        :type prices: List[int]
        :rtype: int
        """
		if len(prices) < 2:
			return 0
		min_price = prices[0]
		profit = prices[1] - prices[0]
		index = 2
		length = len(prices)
		while index < length:
			min_price = min(prices[index - 1], min_price)
			profit = max(profit, prices[index] - min_price)
			index += 1
		if profit < 0:
			profit = 0
		return profit


if __name__ == '__main__':
	solution = Solution()
	print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
