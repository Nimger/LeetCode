# -*- coding:utf-8 -*-

# https://leetcode.com/problems/missing-number/description/


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        return ((1+length)*length/2 - sum(nums))

if __name__ == '__main__':
	solution = Solution()
	print(solution.missingNumber([0]))