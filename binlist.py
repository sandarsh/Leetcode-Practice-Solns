# for i in range(40):
#     print i , bin(i)

arr = [1,2,1,2,12,11]
x = arr[0]
print bin(x)
for i in range(1,(len(arr))):
    x = x ^ arr[i]
    print bin(arr[i])

print bin(x)
