def removeDuplicates(self, nums):
    if not nums:
        return 0
    else:
        current = nums[0]
        start = 1
        end = len(nums)
        while start != end:
            if nums[start] == current:
                del nums[start]
                end -= 1
            else:
                current = nums[start]
                start += 1
        return start
