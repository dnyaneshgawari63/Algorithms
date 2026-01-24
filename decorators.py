# decorators are the extension to the previously written code functionality 

def calc_decorator(func):
  def wrapper(a, b):
    print(a + b)
    print(a - b)
    return func(a,b)
  return wrapper

@calc_decorator
def operate(a, b):
  pass

operate(10,20)

@dec2
    
