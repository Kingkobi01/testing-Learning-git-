class RectangularPrism:
    def __init__(self, length, width, height) -> None:
        self.length = length
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"""Rectangle(length = {self.length}units
Width = {self.width}units
Height = {self.height} units )"""

    def surface_area(self):
        area1 = self.height * self.length
        area2 = self.height * self.width
        area3 = self.width * self.length

        return 2 * (area1 + area2 + area3)

    def volume(self):
        return self.length * self.width * self.height
    


cuboid = RectangularPrism(2,4,6)
cube = RectangularPrism(4,4,4)


assert 48 == cuboid.volume()

assert 96 == cube.surface_area()



