# -*- coding:utf-8 -*-

# https://leetcode.com/problems/merge-sorted-array/description/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()

if __name__ == '__main__':
	solution = Solution()
	nums1 = [1,1,2,3,4]
	solution.merge(nums1,5,[1,3,5,6],4)
	print(nums1)