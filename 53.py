# -*- coding:utf-8 -*-

# https://leetcode.com/problems/maximum-subarray/description/

# Kadane算法,经典的DP问题
class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		max_end = max_result = nums[0]
		if len(nums) <= 1:
			return max_result
		for i in nums[1:]:
			max_end = max(i,max_end+i)
			max_result = max(max_end,max_result)
			print(max_end,max_result)
		return max_result

if __name__ == '__main__':
	solution = Solution()
	print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))