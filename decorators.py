# decorators are the extension to the previously written code functionality 
def decorator(func):
  def wrapper():
    print("abc123")
    result = func()
    print("cde456")
    return result
  return wrapper

@function
def func2():
  return "hahaha"
