
def square_iterator(limit):
  x = 0
  while x < limit:
    yield x*x
    x = x+1

for num in sqaure_iterator(5):
  print(num)
