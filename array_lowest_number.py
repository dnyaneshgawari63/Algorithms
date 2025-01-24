def lowest_val():
  arr = [123,324,34,23,423,23543,65]
  lowest = arr[0]
  for ar in arr:
    if ar < lowest:
      lowest = ar
  return lowest
print(lowest_val())
      
