import random
lot = {}
cars = lot.keys()
spaces = lot.values()
class ParkingLot:
    def __init__(self, name, nspaces):
        self.name = name
        self.nspaces = nspaces
        
    def display(self):
        print("{} has {} spaces".format(self.name, self.nspaces))
        print(lot)

    def park(self,car):
        if len(lot) == self.nspaces:
            print(("There is no space for your {}").format(car))
        else:
            space = random.randint(1,self.nspaces)
            while space in spaces:
                space = random.randint(1,self.nspaces)
            lot.update({car:space})
            print(("Your {} is parked in lot number {}.").format(car, space))
        
    def remove(self, car):
        if car not in cars:
            print("That car is not parked here")
        else:
            lot.pop(car)
            print(("Your {} has left the lot").format(car))
            
p = ParkingLot("Fremont Garage", 3)
p.display()
p.park("Toyota")
p.display()
p.park("Tesla")
p.display()
p.park("BMW")
p.display()
p.park("Ford")
p.display()
p.remove("Tesla")
p.display()
p.park("Ford")
p.display()
