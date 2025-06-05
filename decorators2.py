# here we add at the rate to get the functionality of main function onto out desired

def calculation(anything):
  def wrapper(x, y):
    return x ** y
  return wrapper

@calculation 
def nums(): # decorator takes wrapper function as argument
  return


print(nums(3,4))  #it prints the result from functionality assigned to variables in main function 
print(nums(2.3, 4))
print(nums(5,7))
print()
