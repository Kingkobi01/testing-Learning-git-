class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def __repr__(self) -> str:
        return f"""Rectangle(length = {self.length}units
Width = {self.width}units)"""

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.length + self.width)





rect1 = Rectangle(2,3)

assert 5 != rect1.area()

