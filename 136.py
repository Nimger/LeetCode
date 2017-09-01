# -*- coding:utf-8 -*-

# https://leetcode.com/problems/single-number/description/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums)))*2-sum(nums)

if __name__ == '__main__':
	solution = Solution()
	print(solution.singleNumber([1,1,2,2,3]))