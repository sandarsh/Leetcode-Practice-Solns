def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = len(nums)
    try:
        print nums[l/2-1]
        print nums[l/2]
        print nums[0:l/2]
        print nums[l/2:]
        if nums[l/2-1] >= nums[l/2]:
            return nums[l/2]
        else:
            findMin(nums[0:l/2])
            findMin(nums[l/2:])
            if findMin(nums[0:l/2]) == None:
                return findMin(nums[l/2:])
            else:
                return findMin(nums[0:l/2])
    except:
        pass




arr = [3,4,5,6,7,8,1,2,3]
print findMin(arr)
