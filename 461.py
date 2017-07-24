# -*- coding:utf-8 -*-

def hammingDistance(x, y):
	result = 0
	for index in range(0,32):
		if (x & (1<<index)) ^ (y & (1<<index)):
			result += 1
	return result


if __name__ == '__main__':
	print(hammingDistance(1,4))