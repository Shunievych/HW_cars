import random

class Car:
    def __init__(self, economy, color, model, mileage=0, fuel=100):
        self.mileage = mileage
        self.fuel = fuel
        self.economy = economy
        self.color = color
        self.model = model

    def drive(self, distance):
        required_fuel = distance / self.economy
        if required_fuel > self.fuel:
            raise ValueError("Недостатньо палива для поїздки на таку дистанцію.")
        self.mileage += distance
        self.fuel -= required_fuel

    def distance_left(self):
        return self.fuel * self.economy

    def fuel_up(self):
        self.fuel += 20

colors = ["Purple", "Gray", "Orange", "Brown""Red", "Blue", "Green", "Black", "White", "Yellow"]
models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
economy_values = [random.randint(10, 20) for _ in range(10)]


# Створення списку машин
cars = []
for i in range(10):
    color = random.choice(colors)
    model = random.choice(models)
    economy = random.choice(economy_values)
    car = Car(economy=economy, color=color, model=model)
    cars.append(car)

# Виведення списку машин
for car in cars:
    print(car)


my_car = Car(economy=15, color="Black", model="Toyota Camry")
print(my_car)

try:
    my_car.drive(150)
    print(my_car)
except ValueError as e:
    print(e)

print(f"Залишок дистанції: {my_car.distance_left()} км")

try:
    my_car.drive(1000)
    print(my_car)
except ValueError as e:
    print(e)

my_car.fuel_up()

for car in cars:
    try:
        car.drive(200)
        car.fuel_up()
        car.drive(100)
    except ValueError as e:
        print(f"Помилка: {e}")

# Знайти машину з найбільшим залишком палива
most_fuel_car = max(cars, key=lambda car: car.fuel)

# Знайти максимальну кількість залишку палива
max_fuel = max(car.fuel for car in cars)

# Знайти всі машини з максимальною кількістю залишку палива
cars_with_max_fuel = [car for car in cars if car.fuel == max_fuel]
