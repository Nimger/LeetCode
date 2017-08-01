# -*- coding:utf-8 -*-

# https://leetcode.com/problems/keyboard-row/description/

class Solution(object):
	def findWords(self, words):
		"""
        :type words: List[str]
        :rtype: List[str]
        """
		# # 暴力解法
		# row1 = ['Q','W','E','R','T','Y','U','I','O','P']
		# row2 = ['A','S','D','F','G','H','J','K','L']
		# row3 = ['Z','X','C','V','B','N','M']
		# result = []
		# for letter in words:
		# 	inRow1 = False
		# 	inRow2 = False
		# 	inRow3 = False
		# 	word = letter.upper()
		# 	if word[0] in row1:
		# 		inRow1 = True
		# 	elif word[0] in row2:
		# 		inRow2 = True
		# 	elif word[0] in row3:
		# 		inRow3 = True
		#
		# 	isResult = True
		# 	if inRow1 == True:
		# 		for c in word:
		# 			if c not in row1:
		# 				isResult = False
		# 				break
		# 		if isResult == True:
		# 			result.append(letter)
		#
		# 	if inRow2 == True:
		# 		for c in word:
		# 			if c not in row2:
		# 				isResult = False
		# 				break
		# 		if isResult == True:
		# 			result.append(letter)
		#
		# 	if inRow3 == True:
		# 		for c in word:
		# 			if c not in row3:
		# 				isResult = False
		# 				break
		# 		if isResult == True:
		# 			result.append(letter)
		#
		# return result

		# 集合解法
		line1 = set('qwertyuiop')
		line2 = set('asdfghjkl')
		line3 = set('zxcvbnm')
		result = []
		for word in words:
			w = set(word.lower())
			if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
				result.append(word)
		return result





if __name__ == '__main__':
	solution = Solution()
	print(solution.findWords(['a','b']))
