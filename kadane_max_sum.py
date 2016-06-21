def MaxSum(arr):
    m = arr[0]
    temp = arr[0]
    for each in arr[1:]:
        temp = max(each, temp+each)
        m = max(m,temp)
    return m


arr = [-2,1,-3,4,-1,2,1,-5,4]
m = MaxSum(arr)
print m
