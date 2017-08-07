# -*- coding:utf-8 -*-

# https://leetcode.com/problems/plus-one/description/

class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		index = 0
		length = len(digits)
		# 最后一位+1
		digits[length-1] += 1
		index = len(digits)-1
		#逆序检查数组每一位是否超过10
		while index >= 0:
			if digits[index] >= 10:
				# 考虑第一位是否要进位
				if index == 0:
					digits.insert(0,digits[0]/10)
					digits[1] %= 10
				else:
					digits[index-1] += digits[index]/10
					digits[index] %= 10
			index -= 1
		return digits

if __name__ == '__main__':
	solution = Solution()
	print(solution.plusOne([9,9]))