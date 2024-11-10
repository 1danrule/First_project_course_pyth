class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Vehicle information: vehicle brand - {self.brand}, vehicle model - {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def info(self):
        super().info()
        print(f"Number of doors - {self.num_doors}")


class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def info(self):
        super().info()
        print(f"Type of bike - {self.bike_type}")


class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def info(self):
        super().info()
        print(f"Capacity of truck - {self.capacity}")


car1 = Car('Audi', 'S8', 4)
car2 = Car('Volkswagen', 'Golf', 4)
bike1 = Bike('SCOTT', 'Spark', 'Mountain bike')
bike2 = Bike('Trek', 'Marlin 7', 'Mountain bike')
truck1 = Truck('Volvo', 'FH16', '44 tons')
truck2 = Truck('Mercedes-Benz', 'Actros 1845', '40 tons')
car1.info()
car2.info()
bike1.info()
bike2.info()
truck1.info()
truck2.info()
