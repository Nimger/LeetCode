# -*- coding:utf-8 -*-

# https://leetcode.com/problems/move-zeroes/description/

class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""

		# 删除数组中的0,然后在末尾添加0

		# 简单的写法
		for num in nums:
			if num == 0:
				nums.remove(num)
				nums.append(num)

		# # 繁琐的写法,但是效率好像比上一中高一点
		# index = 0
		# length = len(nums)
		# tempLen = length
		# while index < tempLen:
		# 	if nums[index] == 0:
		# 		nums.remove(0)
		# 		tempLen -= 1
		# 		index -= 1
		# 	index += 1
		# zeroCount = length - len(nums)
		# index = 0
		# while index < zeroCount:
		# 	nums.append(0)
		# 	index += 1

if __name__ == '__main__':
	solution = Solution()
	nums = [0,0,1,2,3,4]
	solution.moveZeroes(nums)
	print(nums)