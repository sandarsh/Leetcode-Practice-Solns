def RodCuttingRecurse(prices,n):
    if n == 0:
        return 0.0
    else:
        maximum = prices[n]
        for i in range(1,n):
            price = prices[i] + RodCuttingRecurse(prices, n-i)
            if price > maximum:
                maximum = price
        return maximum

def RodCuttingDP(prices,n):
    arr = [0 for x in range(n+1)]
    print arr
    arr[0] = 0
    for i in range(1,n+1):
        maximum = prices[i]
        for j in range(1,i):
            temp = prices[j] + arr[i-j]
            print temp , maximum
            if temp > maximum:
                maximum = temp
                # print j, i-j
                # print prices[j] , arr[i-j]
                # print maximum
                # print ""
        arr[i] = maximum
        print arr
    return arr[n]



prices = [0,1,3,3,5,5,10,8,3,10,10]
n = 10
#maximum = RodCuttingRecurse(prices,n)
max2 = RodCuttingDP(prices,n)
# print maximum
# print max2
