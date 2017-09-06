# -*- coding:utf-8 -*-

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_set = set(nums)
        length = len(nums)
        mis_num = length*(length+1)/2-sum(nums_set)
        same_num = mis_num-(length*(length+1)/2-sum(nums))
        return [int(same_num),int(mis_num)]

if __name__ == '__main__':
	solution = Solution()
	print(solution.findErrorNums([1,2,2,4]))
