def reverse(x):
    y = x
    x = abs(x)
    num = 0
    while x != 0:
        num = (num * 10) + (x % 10)
        x /= 10
    if num > 2147483647:
        return 0
    elif y >= 0:
        return num
    else:
        return -num
