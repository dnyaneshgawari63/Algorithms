# Here we add the lowest value before the greter value in 

def select_sort(array):
  n = len(array)
  for x in range(n-1):
    min_index = x
    for y in range(x+1, n):
      if array[y] < array[min_index]:
        min_index = y
    min_value = array.pop(min_index)
    array.insert(x, min_value)
  return array

select_sort([12,455,43,2,44,56])
