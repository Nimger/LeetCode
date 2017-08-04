# -*- coding:utf-8 -*-

class Solution(object):
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		# O(n)的排序,然后找出消失的数字
		result = []
		i = 0
		length = len(nums)
		while i < length:
			if nums[i] != i+1:
				index = nums[i]-1
				if nums[i] != nums[index]:
					nums[i],nums[index] = nums[index],nums[i]
					if i != 0:
						i -= 1
				else:
					i += 1
			else:
				i += 1
		for i in range(1,len(nums)+1):
			if i != nums[i-1]:
				result.append(i)
		return result

if __name__ == '__main__':
	solution = Solution()
	print(solution.findDisappearedNumbers([1,1]))