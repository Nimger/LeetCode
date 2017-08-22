# -*- coding:utf-8 -*-

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        index = 0
        lenght = len(flowerbed)
        while index < len(flowerbed):
            if(flowerbed[index] == 0 and (index == 0 or flowerbed[index-1] == 0) and (index == lenght-1 or flowerbed[index+1] == 0)):
                n -= 1
                flowerbed[index] = 1
            index += 1
        return n <= 0

if __name__ == '__main__':
	solution = Solution()
	print(solution.canPlaceFlowers([1,0,0,0,0],2))