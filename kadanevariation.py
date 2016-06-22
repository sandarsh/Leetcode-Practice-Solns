# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/maxsubarray
k = int(raw_input().strip())
for i in range(k):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(" "))
    nc_sum = arr[0]
    temp = arr[0]
    max_sum = arr[0]
    for j in range(1,n):
        temp = max(arr[j], temp+arr[j])
        max_sum = max(temp, max_sum)
        if arr[j] < 0:
            nc_sum = max(nc_sum, arr[j])
        else:
            nc_sum = max(arr[j], nc_sum+arr[j])
    print max_sum, nc_sum
