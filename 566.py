# -*- coding:utf-8 -*-

# https://leetcode.com/problems/reshape-the-matrix/description/

class Solution(object):
	def matrixReshape(self, nums, r, c):
		"""
		:type nums: List[List[int]]
		:type r: int
		:type c: int
		:rtype: List[List[int]]
		"""
		length = 0
		totalList = []
		for list in nums:
			length += len(list)
			totalList.extend(list)
		if length != r*c:
			return nums

		result = []
		for i in range(0,len(totalList),c):
			result.append(totalList[i:i+c])
		return result



if __name__ == '__main__':
	solution = Solution()
	print(solution.matrixReshape([[1,2],[3,4]],1,4))