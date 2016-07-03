#https://leetcode.com/submissions/detail/65974820/

def countNumbersWithUniqueDigits(n):
    if n==0:
        return 1
    elif n == 1:
        return 10
    elif n == 2:
        return 9*9 + countNumbersWithUniqueDigits(n-1)
    else:
        uniques = 0
        sum = 0
        temp = 81
        for i in range(3,n+1):
            temp *= (11-i)
            sum += temp
        return sum + countNumbersWithUniqueDigits(2)
