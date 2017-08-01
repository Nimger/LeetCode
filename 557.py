# -*- coding:utf-8 -*-

# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		result = []
		list = s.split(' ')
		for word in list:
			result.append(word[::-1])
		resultStr = ' '.join(result)
		return resultStr

if __name__ == '__main__':
	solution = Solution()
	print(solution.reverseWords("Let's take LeetCode contest"))