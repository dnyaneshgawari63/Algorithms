# we will be finding the element out of an array using binary sort with time complexity used Ologbase2n

array = [1323,34,43,323,4,54,57,56,22,332,32,23,1313,133,12]
array.sort()
left = 0
right = len(array) - 1
Target = 34
found = None # or we can give -1

while left <= right:
    mid = ( left + right ) // 2
    if array[mid] == Target:
        found = mid
        break
    elif array[mid] < Target:
        left  = mid + 1
    else:
        right = mid - 1
print(array)
print(found)
