class Car:
    def __init__(self, year: int, maker: str, mark: str, consumption: float):
        self.year = year
        self.maker = maker
        self.mark = mark
        self.run = 0
        self.consumption = consumption


    def drive(self):
        return f"I have a car of the brand {self.mark}, I go on the owner's errands"

    @property
    def cost_of_service(self):
        return self.run * 7.6

car1 = Car(1909, 'August Horch', 'Audi', 4.5)
car2 = Car(1930, 'Josef Ganz', 'Volkswagen', 4.5)
car3 = Car(1933, 'Kiichiro Toyoda', 'Volkswagen', 4.5)

car2.run = 5500

print(car1.drive())
print(car2.cost_of_service)
