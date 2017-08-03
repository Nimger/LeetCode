# -*- coding:utf-8 -*-

# https://leetcode.com/problems/reverse-string/description/

class Solution(object):
	def reverseString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		return s[::-1]


if __name__ == '__main__':
	solution = Solution()
	print(solution.reverseString('hello'))