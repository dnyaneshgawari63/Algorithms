def calculation(generic):
  def wrapper(x, y):
    return x ** y
  return wrapper

@calculation
def nums():
  return

print(nums(3,4))
