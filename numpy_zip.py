# with zip inbuilt method we can do sum of two arrays

list = [2,4,55,3]
list2 = [2,43,5,5]

import numpy as np

list3 =[]

for x , y in zip(list, list2):
  list3.append(x+y)
print(list3)
