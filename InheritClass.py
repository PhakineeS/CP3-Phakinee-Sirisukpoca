class Vehicle:
    licenseNumber = ''
    serialCode = ''

    def turnOnAir(self):
        print("Turn on air conditioner")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World")

class PickUp(Vehicle):
    def sayHello(self):
        print("Hello Mars")

class Truck(Vehicle):
    def sayHello(self):
        print("Hello Jupiter")

class Estate(Vehicle):
    def sayHello(self):
        print("Hello Venus")

car1 = Car()
car1.turnOnAir()
car1.sayHello()

print()

pickUp1 = PickUp()
pickUp1.turnOnAir()
pickUp1.sayHello()

print()

truck1 = Truck()
truck1.turnOnAir()
truck1.sayHello()

print()

estate1 = Estate()
estate1.turnOnAir()
estate1.sayHello()
