import random
def pivot(nums):
    print nums
    n = len(nums) - 1
    pivot = random.randint(0 , n)
    print "Pivot is" , pivot
    temp = nums[pivot]
    nums[pivot] = nums[n]
    nums[n] = temp
    pivot = n
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
    print pivot

def ArrayLShift(arr,ins,dt):
    temp = arr[dt]
    item = dt
    for item in range(dt,ins):
        arr[item] = arr[item + 1]
    arr[ins] = temp
    return arr

arr = [1,4,3,5,7,2,8,6,9,8,10]
pivot(arr)
print arr[3:]
