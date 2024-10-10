def find(arr, target):
    for x in range(len(arr)):
        if arr[x] == target:
            return x
    return -1

arr = [10,11,12,13,14,15,16,17,18,19,20] 
target = 14
print(find(arr, target))