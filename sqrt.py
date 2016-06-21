##Calculates the square root of x correct to 10 decimal places
##Change 'e' in line 9 to increase or reduce accuracy
def mySqrt(x):
    if x <= 1:
        return x
    else:
        e = 2
        y = x/2.0
        temp = x
        while y**2 != x and e > 0.00000000001:
            if y**2 > x:
                temp = y
                y /= 2.0
                print y
            else:
                e = abs(y-temp)
                y = (temp + y)/2.0
                print y
        return y

x = 39
print mySqrt(x)
