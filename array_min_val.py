arr = [123,43,123,45,6,76,78,34]

lowest = arr[0]
for x in arr:
  if x < lowest:
    lowest = x
print(lowest)
