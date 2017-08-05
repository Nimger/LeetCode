# -*- coding:utf-8 -*-

# https://leetcode.com/problems/contains-duplicate/description/

# 利用集合的特性不重复,然后比较集合的长度和数组的长度
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        if len(nums_set) < len(nums):
            return True
        else:
            return False

if __name__ == '__main__':
	pass