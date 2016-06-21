import random


def findKthLargest(nums, k):
    print "New call"
    print nums
    req_index = k-1
    n = len(nums) - 1
    pivot = random.randint(0,n)
    print "Random pivot is" , pivot
    temp = nums[pivot]
    nums[pivot] = nums[n]
    nums[n] = temp
    pivot = n
    print "Pivot is" , pivot
    print nums
    for index in range(n,0,-1):
        myind = index - 1
        if nums[pivot] <= nums[myind]:
            print nums
            pass
        elif nums[pivot] > nums[myind]:
            ArrayLShift(nums,pivot,myind)
            pivot -= 1
            print nums
    if pivot == req_index:
        return nums[req_index]
    elif pivot < req_index:
        return findKthLargest(nums[pivot+1:], k- (pivot + 1))
    elif pivot > req_index:
        return findKthLargest(nums[0:pivot] , k)

def ArrayLShift(arr,ins,dt):
    temp = arr[dt]
    item = dt
    for item in range(dt,ins):
        arr[item] = arr[item + 1]
    arr[ins] = temp
    return arr

myarr = [1,2,3,4,5,6,7,8,9]
k = 9
findKthLargest(myarr,k)
