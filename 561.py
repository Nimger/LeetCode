# -*- coding:utf-8 -*-

# https://leetcode.com/problems/array-partition-i/#/description

class Solution(object):
	def arrayPairSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		list = sorted(nums)
		result = 0
		for index,value in enumerate(list):
			if index%2 == 0:
				result += value
		return result


if __name__ == '__main__':
	solution = Solution()
	result = solution.arrayPairSum([1,4,3,2])
	print(result)