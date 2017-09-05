# -*- coding:utf-8 -*-
import collections

# https://leetcode.com/problems/number-of-boomerangs/description/

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for x1,y1 in points:
            dmap = collections.defaultdict(int)
            for x2,y2 in points:
                dmap[(x1 - x2) ** 2 + (y1 - y2) ** 2] += 1
            for d in dmap:
                result += dmap[d]*(dmap[d]-1)
        return result

if __name__ == '__main__':
	solution = Solution()
	print(solution.numberOfBoomerangs([[0,0],[1,0],[2,0]]))