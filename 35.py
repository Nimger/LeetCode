# -*- coding:utf-8 -*-

# https://leetcode.com/problems/search-insert-position/description/

class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if nums[0] > target:
			return 0
		if nums[len(nums)-1] < target:
			return len(nums)
		index = 0
		for num in nums:
			if num == target:
				return index
			elif num > target:
				return max(0,index)
			else:
				index += 1
		return index

if __name__ == '__main__':
	solution = Solution()
	print(solution.searchInsert([1,3,5,6],7))