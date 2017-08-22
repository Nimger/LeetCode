# -*- coding:utf-8 -*-

# https://leetcode.com/problems/distribute-candies/description/

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kinds = set(candies)
        return min(len(kinds),len(candies)/2)

if __name__ == '__main__':
	solution = Solution()
	print(solution.distributeCandies([1,1,2,2,3,3]))