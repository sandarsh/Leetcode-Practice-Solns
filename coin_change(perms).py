##Number of ways in which an amout can be changed given
##the denominations

def coinChange(coins,amt):
    coins.sort(reverse=True)
    arr = [[0 for i in range(amt+1)] for j in range(len(coins))]
    for i in range(len(coins)):
        for j in range(amt+1):
            if j == 0:
                arr[i][j] = 1
            elif j % coins[i] == 0 and i == 0:
                arr[i][j] = 1
            elif j < coins[i]:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-coins[i]]

    return arr



coins = [1,2,3]
amt = 5
print coinChange(coins,amt)
