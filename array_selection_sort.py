# Here we add the lowest value before the greter value in the array

array = [12,43,2,44,5,6,7,53,3,6,6]

def select_sort():
  n = len(array)
  for x in range(n-1):
    min_index = x
    for y in range(x+1, n):
      if array[y] < array[min_index]:
        min_index = y
    min_value = array.pop(min_index)
    array.insert(x, min_value)
  return array

select_sort()
