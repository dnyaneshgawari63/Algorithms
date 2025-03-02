def insertsort(array):
  n = len(array)
  for x in range(1, n):
    insert_ind = x
    current_val = array.pop(x)
    for y in range(x-1, -1, -1):
      if array[y] > current_val:
        insert_ind = y
    array.insert(insert_ind, current_val)
    return array

insertsort(array)
