def insertsort(array):
  n = len(array)
  for x in range(1, n):
    insert_ind = x
    current_val = array.pop(x)
