from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self, area):
        print(("area is {}").format(area))
    @abstractmethod
    def perimeter(self, perimeter):
        print(("perimeter is {}").format(perimeter))

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
        
    def area(self):
        area = 3.14*self.radius*self.radius
        super().area(area)

    def perimeter(self):
        perimeter = 6.28 * self.radius
        super().perimeter(perimeter)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length*self.width
        super().area(area)
        
    def perimeter(self):
        perimeter = 2*(self.length+self.width)
        super().perimeter(perimeter)

c = Circle(5)
c.area()
c.perimeter()
r = Rectangle(5,6)
r.area()
r.perimeter()

