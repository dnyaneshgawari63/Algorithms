class ArithmeticOperation: #Base class
    def calculate(self, x, y):
        raise NotImplementedError("Subclasses must implement this method")

class Addition(ArithmeticOperation):
    def calculate(self, x, y):
        return x + y

class Subtraction(ArithmeticOperation):
    def calculate(self, x, y):
        return x - y

class Multiplication(ArithmeticOperation):
    def calculate(self, x, y):
        return x * y

class Division(ArithmeticOperation):
    def calculate(self, x, y):
        if y == 0:
            return "Division by zero error!"
        return x / y

# Example
add = Addition()
print(f"Addition: {add.calculate(5,3)}") # Output: Addition: 8

mult = Multiplication()
print(f"Multiplication: {mult.calculate(10, 2)}") # Output: Multiplication: 20
