class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting.")

# use the class
my_car = Car("Toyota")
print(my_car.brand)
my_car.start()