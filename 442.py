# -*- coding:utf-8 -*-

# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
	def findDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		result = set()
		i = 0
		while i < len(nums):
			if nums[i] != i+1:
				index = nums[i]-1
				if nums[i] != nums[index]:
					nums[i],nums[index] = nums[index],nums[i]
					i -= 1
				else:
					result.add(nums[i])
			i += 1
		result_list = list(result)
		return result_list

if __name__ == '__main__':
	solution = Solution()
	print(solution.findDuplicates([4,3,2,7,8,2,3,1]))