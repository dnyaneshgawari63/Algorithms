# In generators, we use the keywork yeild
# Lazy evaluation: its memory efficient and good when we have huge amount of dataset

def square_iterator(limit):
  x = 0
  while x < limit:
    yield x*x
    x = x+1

for num in square_iterator(5):
  print(num)
