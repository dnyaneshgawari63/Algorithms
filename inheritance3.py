class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.year} {self.brand} {self.model} starts.")

    def describe(self):
        print(f"This is a {self.year} {self.brand} {self.model}.")

class Toyota(Car):
    def hybrid_system(self):
        print(f"The {self.brand} {self.model} has a hybrid system.")

class Ford(Car):
    def truck_mode(self):
        print(f"The {self.brand} {self.model} can be used in truck mode.")

class Tesla(Car):
    def autopilot(self):
        print(f"The {self.brand} {self.model} has autopilot capabilities.")


# Example usage
toyota = Toyota("Toyota", "Prius", 2023)
toyota.start()  # Output: The 2023 Toyota Prius starts.
toyota.hybrid_system()  # Output: The Toyota Prius has a hybrid system.
toyota.describe()
