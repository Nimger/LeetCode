# -*- coding:utf-8 -*-

# https://leetcode.com/problems/majority-element/description/

# 出现不同的元素,则两两抵消,相当于从数组移除,剩下的那一个一定就是要找的那个元素
class Solution(object):
	def majorityElement(self, nums):
		"""
        :type nums: List[int]
        :rtype: int
        """
		count = 1
		element = nums[0]
		if len(nums) <= 1:
			return element
		for num in nums[1:]:
			if count == 0:
				element = num
				count = 1
			else:
				if element == num:
					count += 1
				else:
					count -= 1
		return element


if __name__ == '__main__':
	solution = Solution()
	print(solution.majorityElement([1]))
