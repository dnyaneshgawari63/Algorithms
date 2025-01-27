def calculation(generic):
  def wrapper(x, y):
    return x ** y
  return wrapper

@calculation
def nums(x, y):
  return 3,5
