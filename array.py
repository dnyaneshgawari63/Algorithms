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
def reverse(aaa):
    aaa.sort()
    return aaa[::-1]
array = [10,1111,12,1332,14,150,16,17,180,19,220]

    




