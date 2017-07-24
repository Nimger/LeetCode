# -*- coding:utf-8 -*-

def twoSum(nums,target):
    result = []
    index = 0
    for index,num in enumerate(nums):
        # print(index)
        otherNum = target-num
        # print(nums[index:])
        if otherNum in nums[index+1:]:
            otherIndex = nums[index+1:].index(otherNum)
            if otherIndex+index+1 > index:
                result = [index,otherIndex+index+1]
                return result
    return result


if __name__ == '__main__':
	nums = [3,3]
	target = 6
	print(twoSum(nums,target))