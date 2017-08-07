# -*- coding:utf-8 -*-

# https://leetcode.com/problems/remove-element/description/

class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		index = 0
		while index < len(nums):
			if nums[index] == val:
				nums.remove(val)
				index -= 1
			index += 1
		return len(nums)

if __name__ == '__main__':
	solution = Solution()
	print(solution.removeElement([3,3],3))