# static method is a built in method where we dont need self parameter and init method to create instance and call it. Instead static method directly calls the respective function.

class Calc:
  @staticmethod
  def add(a,b):
    return a * b

  @staticmethod
  def subs(a,b):
    return a - b

result = Calc.add(23,34)
result2 = Calc.subs(123-10)

print(result, result2)

