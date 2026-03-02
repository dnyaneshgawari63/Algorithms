# simplified version

list = [5,1,4,2,7,6,9,8,10]

for x in range(len(list)-1):
  for y in range(len(list)-x-1):
    if list[y] > list[y+1]:
      list[y], list[y+1] = list[y+1], list[y]

print(list)
