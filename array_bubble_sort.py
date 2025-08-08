⁴array = [123,321,324,324,243,56,87,934,789,980]

n = len(array)

for x in range(n-1):
  swapped = False
  for y in range(n-x-1):
    if array[y] > array[y+1]:
      array[y], array[y+1] = array[y+1], array[y]
      swapped = True
  if not swapped:
      break

print(array)
