def ArrayLShift(arr,ins,dt):
    temp = arr[dt]
    item = dt
    for item in range(dt,ins):
        arr[item] = arr[item + 1]
        print item
    arr[ins] = temp
    return arr

def ArrayRShift(arr,ins,dt):
    temp = arr[dt]
    item = dt
    for item in range(dt,ins,-1):
        arr[item] = arr[item - 1]
        print item
    arr[ins] = temp
    return arr


def ArrayShift(arr,ins,dt):
    if dt < ins:
        return ArrayLShift(arr,ins,dt)
    else:
        return ArrayRShift(arr,ins,dt)

myarray = [0,1,2,3,4,5,6,7,8,9]
ins = 6
dt = 3
print myarray
myarray = ArrayShift(myarray,ins,dt)
print myarray
