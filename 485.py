# -*- coding:utf-8 -*-

# https://leetcode.com/problems/max-consecutive-ones/description/

class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		result = 0
		count = 0
		for num in nums:
			if num == 1:
				count += 1
			else:
				# 当元素是0的时候,统计前面1的最大个数,个数统计归0
				result = max(count,result)
				count = 0
		# 如果最后一个元素是1的话,统计会出错
		result = max(count,result)
		return result



if __name__ == '__main__':
	solution = Solution()
	print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))