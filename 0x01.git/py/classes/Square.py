class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def __repr__(self) -> str:
        return f"Square(side length = {self.side_length} units)"

    def area(self):
        return self.side_length**2

    def perimeter(self):
        return 4 * self.side_length




square_1 = Square(4)
square_2 = Square(5)
square_3 = Square(10)

assert 16 == square_1.area()
assert 20 == square_2.perimeter()

assert "Square(side length = 10 units)" == str(square_3)
