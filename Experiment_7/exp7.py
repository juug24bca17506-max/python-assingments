class Vehicle:
    def __init__(self, name):
        self.name = name

    def start(self):
        print("Vehicle starts")


class Car(Vehicle):
    def start(self):
        print(self.name, "car starts with key")


class ElectricCar(Car):
    def charge(self):
        print(self.name, "is charging")


class GPS:
    def location(self):
        print("Tracking location")


class MusicSystem:
    def play_music(self):
        print("Playing music")


class SmartCar(GPS, MusicSystem):
    def features(self):
        print("Smart car has GPS and Music System")


class Bike(Vehicle):
    def start(self):
        print(self.name, "bike starts with kick")


class Truck(Vehicle):
    def start(self):
        print(self.name, "truck starts with button")


class HybridCar(Car, GPS):
    def features(self):
        print(self.name, "has hybrid features")


c = Car("Honda")
e = ElectricCar("Tesla")
b = Bike("Yamaha")
t = Truck("Volvo")
s = SmartCar()
h = HybridCar("Toyota")

c.start()

e.start()
e.charge()

b.start()
t.start()

s.location()
s.play_music()
s.features()

h.start()
h.location()
h.features()