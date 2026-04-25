from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        return (2 * self.height + 2 * self.width)
    
    def describe(self):
        print(self.area())
        print(self.perimeter())


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (math.pi * self.radius**2)

    def perimeter(self):
        return (2 * math.pi * self.radius)
    
    def describe(self):
        print(self.area())
        print(self.perimeter())

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base * self.height)/2

    def perimeter(self):
        return 

    def describe(self):
        print(self.area())
        print(self.perimeter())

if __name__ == "__main__":
    cir = Circle(5)
    cir.describe()
    print("\n")
    tri = Triangle(4, 5)
    tri.describe()
    print("\n")
    rec = Rectangle(3,5)
    rec.describe()
