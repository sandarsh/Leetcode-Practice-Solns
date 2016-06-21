##Fewest number of coins required to make the amount
def coinChange(coins,amount):
    if amount == 0:
            return -1
    else:
        val_coins = []
        for item in coins:
            if item < amount:
                val_coins.append(item)
        coins = val_coins
        if coins:
            coins.sort(reverse=True)
            arr = [[float('inf') for j in range(amt+1)] for i in range(len(coins))]
            for i in range(len(coins)):
                for j in range(amt+1):
                    if j == 0:
                        arr[i][j] = 0
                    elif i == 0 and j % coins[i] == 0:
                        arr[i][j] = j / coins[i]
                    elif coins[i] == j:
                        arr[i][j] = 1
                    else:
                        arr[i][j] = min(arr[i-1][j],(arr[i][j-coins[i]] + 1))
            if arr[len(coins)-1][amount] != float('inf'):
                return arr[len(coins)-1][amt]
            else:
                return -1
        else:
            return -1

#[259,78,94,130,493,4,168,149]
#4769
coins = [259,78,94,130,493,4,168,149]
amt = 4769
arr = coinChange(coins,amt)
print arr
