# Here we add the lowest value before the greter value in the array

def select_sort():
  n =len(array)
  for x in range(n-1):
    min_index = x
    for y in range(x+1, n):
