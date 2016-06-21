def LongestIncSubs(arr):
    l = len(arr)
    temp = [1 for k in range(l)]
    for i in range(l):
        for j in range(i):
            if arr[i] > arr[j]:
                temp[i] = max(temp[i],temp[j] + 1)
    return max(temp)





arr = [1,3,6,7,9,4,10,5,6]
length = LongestIncSubs(arr)
print length
