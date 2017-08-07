# -*- coding:utf-8 -*-

# https://leetcode.com/problems/pascals-triangle/description/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        result = [[1],[1,1]]
        index = 2
        while index < numRows:
            array = [1 for i in range(index+1)]
            for i,num in enumerate(result[index-1]):
                if i >= 1:
                    array[i] = result[index-1][i]+result[index-1][i-1]
            result.append(array)
            index += 1
        return result

if __name__ == '__main__':
	solution = Solution()
	print(solution.generate(5))