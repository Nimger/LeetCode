# -*- coding:utf-8 -*-

def twoSum(nums,target):
    result = []
    for index,num in enumerate(nums):
        otherNum = target-num
        if otherNum in nums[index+1:]:
            otherIndex = nums[index+1:].index(otherNum)
            return [index,otherIndex+index+1]
    return result


if __name__ == '__main__':
    nums = [3,3]
    target = 6
    print(twoSum(nums,target))