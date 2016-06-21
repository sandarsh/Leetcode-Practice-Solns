import sys

def twoSum(nums, target):
        mydict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in mydict.keys():
                print mydict
                return [mydict[target-nums[i]] ,i]
            else:
                mydict[nums[i]] = i

nums = [1,2,3,4,5,6,7,8,9, 10,11,12,13,14,15,16,17,18,19]
target = 37
print twoSum(nums, target)
