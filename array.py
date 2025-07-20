# finding an element in array
def find(array, target):
    for x in range(len(array)):
        if array[x] == target:
            return x
    return -1

array = [10,11,12,13,14,15,16,17,18,19,20] 
target = 14
print(find(array, target))

# example 2





