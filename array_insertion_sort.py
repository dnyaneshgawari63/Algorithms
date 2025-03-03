# sort array using insert sort method
def abc(array):
    n = len(array)
    for x in range(1, n):
        insert_ind = x
        current_val = array.pop(x)
        for y in range(x-1, -1, -1):
            if array[y] > current_val:
                insert_ind = y
        array.insert(insert_ind, current_val)
    return array

array = [213,543,53,23,34,2133,423,45,334,23,343,5454,4,46556]
abc(array)
