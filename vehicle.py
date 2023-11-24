class Vehicle():
    wheels = 0
    passengers = 0

    def wheels(self):
        print((("{} has {} wheels").format(self.name, self.wheels)).capitalize())


    def passengers(self):
        print(("There can be {} passengers in {}").format(self.passengers,self.name))

class Car(Vehicle):
    name = "car"
    def wheels(self):
        self.wheels = 4
        super().wheels()

    def passengers(self):
        self.passengers = 5
        super().passengers()

class Truck(Vehicle):
    name = "truck"
    def wheels(self):
        self.wheels = 4
        super().wheels()

    def passengers(self):
        self.passengers = 2
        super().passengers()

class Motercycle(Vehicle):
    name = "motercycle"
    def wheels(self):
        self.wheels = 2
        super().wheels()

    def passengers(self):
        self.passengers = 2
        super().passengers()

class Bus(Vehicle):
    name = "bus"
    def wheels(self):
        self.wheels = 4
        super().wheels()

    def passengers(self):
        self.passengers = 20
        super().passengers()

c = Car()
c.wheels()
c.passengers()
t = Truck()
t.wheels()
t.passengers()
m = Motercycle()
m.wheels()
m.passengers()
b = Bus()
b.wheels()
b.passengers()
