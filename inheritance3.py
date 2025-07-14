class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print({self.year} {self.brand} {self.model})

    def describe(self):
        print({self.year} {self.brand} {self.model})

class Toyota(Car):
    def hybrid_system(self):
        print({self.brand} {self.model}.)

class Ford(Car):
    def truck_mode(self):
        print( )

class Tesla(Car):
    def autopilot(self):
        print(self.brand}, self.model)


# Example usage
toyota = Toyota("Toyota", "Prius", 2023)
toyota.start()
toyota.hybrid_system()  
toyota.describe()

