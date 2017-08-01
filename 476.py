# -*- coding:utf-8 -*-

def findComplement(num):
	for index in range(0,32):
		if (num & (1<<(31-index))):
			num = ~num & ((1<<(31-index+1))-1)
			break
	return num



if __name__ == '__main__':
	print(findComplement(5))