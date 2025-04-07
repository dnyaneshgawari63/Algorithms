# here

def calculation(anything):
  def wrapper(x, y):
    return x ** y
  return wrapper

@calculation 
def nums(): # decorator takes wrapper function as argument
  return

print(nums(3,4))
