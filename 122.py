# -*- coding:utf-8 -*-

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution(object):
	def maxProfit(self, prices):
		"""
        :type prices: List[int]
        :rtype: int
        """
		profit = 0
		index = 1
		length = len(prices)
		while index < length:
			if prices[index] > prices[index - 1]:
				profit += (prices[index] - prices[index - 1])
			index += 1
		return profit


if __name__ == '__main__':
	solution = Solution()
	print(solution.maxProfit([1, 2, 4]))
