# -*- coding:utf-8 -*-

def findComplement(num):
	# num = ~num
	# start = False
	for index in range(0,32):
		if (num & (1<<(31-index))):
			print(1<<(31-index))
			print((1<<(31-index+1))-1)
			num = ~num & ((1<<(31-index+1))-1)
			break
	return num



if __name__ == '__main__':
	print(findComplement(5))