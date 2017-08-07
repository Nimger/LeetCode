# -*- coding:utf-8 -*-

# https://leetcode.com/problems/rotate-array/description/

class Solution(object):
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		length = len(nums)
		result = nums[length-k:]+nums[0:length-k]
		for i in range(length):
			nums[i] = result[i]

if __name__ == '__main__':
	solution = Solution()
	nums = [1,2]
	solution.rotate(nums,1)
	print(nums)