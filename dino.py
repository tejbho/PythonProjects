class Dinosaur:
    def __init__(self, name, diet):
        self.name = name
        self.diet = diet
        
    def __str__(self):
        return ((("I am a {}. I am a {}.").format(self.name,self.diet)).replace('_', " "))

    def timeperiod(self):
        print("Mezezoic")
        
class Stegosaurus(Dinosaur):
    def __init__(self):
        super().__init__("Stegosaurus", "herbivore")

    def timeperiod(self):
        print("Jurrasic")
    

class Tyranasaurus_Rex(Dinosaur):
    def __init__(self):
        super().__init__("Tyranasaurus_Rex", "carnivore")

    def timeperiod(self):
        print("Cretaceus")

class Velociraptor(Dinosaur):
    def __init__(self):
        super().__init__("Velociraptor", "carnivore")

    def timeperiod(self):
        print("Cretaceus")

class Triceratops(Dinosaur):
    def __init__(self):
        super().__init__("Triceratops", "herbivore")

    def timeperiod(self):
        print("Cretaceous")

s = Stegosaurus()
print(s)
s.timeperiod()
t = Tyranasaurus_Rex()
print(t)
t.timeperiod()
v = Velociraptor()
print(v)
v.timeperiod()
x = Triceratops()
print(x)
x.timeperiod()
