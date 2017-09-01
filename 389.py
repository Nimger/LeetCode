# -*- coding:utf-8 -*-

# https://leetcode.com/problems/find-the-difference/description/

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_num = 0
        t_num = 0
        for word in s:
            s_num += ord(word)
        for word in t:
            t_num += ord(word)
        return chr(t_num - s_num)

if __name__ == '__main__':
	solution = Solution()
	print(solution.findTheDifference('abcd','abcde'))