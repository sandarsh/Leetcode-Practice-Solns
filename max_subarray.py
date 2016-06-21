##Problem from interview bit
##To find the maximum positive sums discarding the negatives
def maxset(A):
    subarrays = []
    start = 0
    i=0
    while i != len(A):
        if A[i] < 0:
            subarrays.append(A[start:i])
            start = i + 1
        if i == len(A)-1:
            subarrays.append(A[start:i+1])
        i += 1
    lenth = []
    sums = []
    print subarrays
    for each in range(len(subarrays)):
        leng = len(subarrays[each])
        lenth.append(leng)
        mysum = 0
        for i in range(len(subarrays[each])):
            mysum = mysum + subarrays[each][i]
        sums.append(mysum)
    print sums
    print lenth
    max_ind = sums.index(max(sums))
    print max_ind
    print subarrays[max_ind]
    return subarrays[max_ind]


A = [-1,1,2,3,4,-3,-3,-3,2,3,4,-4,2,5,6,-3]
maxset(A)
