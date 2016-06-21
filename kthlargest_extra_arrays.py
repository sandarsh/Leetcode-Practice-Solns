
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    n = len(nums)
    pivot = random.randint(0,n-1)
    l_count = 0
    g_count = 0
    less_arr = []
    greater_arr = []
    mid = nums[pivot]
    for index in range(0,n):
        if index != pivot:
            if nums[index]>mid:
                greater_arr.append(nums[index])
                g_count += 1
            else:
                less_arr.append(nums[index])
                l_count += 1
        else:
            pass
    if k == g_count+1:
        return mid
    elif k > g_count+1:
        return findKthLargest(less_arr, k-(g_count+1))
    elif k < g_count+1:
        greater_arr.append(mid)
        return findKthLargest(greater_arr , k)
