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
toyota.describe() # Output: This is a 2023 Toyota Prius.

ford = Ford("Ford", "F-150", 2024)
ford.start()  # Output: The 2024 Ford F-150 starts.
ford.truck_mode()  # Output: The Ford F-150 can be used in truck mode.
ford.describe() # Output: This is a 2024 Ford F-150.

tesla = Tesla("Tesla", "Model S", 2022)
tesla.start()  # Output: The 2022 Tesla Model S starts.
tesla.autopilot()  # Output: The Tesla Model S has autopilot capabilities.
tesla.describe() # Output: This is a 2022 Tesla Model S.
