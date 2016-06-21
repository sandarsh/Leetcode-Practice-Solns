def ArrayRShift(arr,ins,dt):
    temp = arr[dt]
    item = dt
    for item in range(dt,ins,-1):
        arr[item] = arr[item - 1]
        print item
    arr[ins] = temp
    return arr

myarray = [1,2,3,4,5,6,7,8,9]
ins = 3
dt = 4
myarray = ArrayRShift(myarray,ins,dt)
print myarray
