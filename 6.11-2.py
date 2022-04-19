import  math


class Circle:
    def __init__(self, r=0):
        self.r = r

    def get_area(self):
        return math.pi * self.r ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.r


c = Circle(4.44)
print(c.get_perimeter())
print(c.get_area())