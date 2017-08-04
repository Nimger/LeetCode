# -*- coding:utf-8 -*-

class Solution(object):
	def twoSum(self, numbers, target):
		"""
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
		# # 会超时
		# index = 0
		# while index < len(numbers):
		# 	result = target - numbers[index]
		# 	i = index
		# 	while i < len(numbers):
		# 		if numbers[i] == result and i != index:
		# 			return [index + 1, i + 1]
		# 		i += 1
		# 	index += 1

		# 首尾聚拢
		l, r = 0, len(numbers) - 1
		while l < r:
			s = numbers[l] + numbers[r]
			if s == target:
				return [l + 1, r + 1]
			elif s < target:
				l += 1
			else:
				r -= 1


if __name__ == '__main__':
	solution = Solution()
	print(solution.twoSum([3, 7, 9], 10))
