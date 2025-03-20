import numpy as np

def add(x, y):
  return x + y

result = np.frompyfunc(add, 2, 1)
result([12,3,4],[1,2,3])
