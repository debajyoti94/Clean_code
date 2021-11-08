class Point:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


class Rectangle:
    def __init__(self, starting_point, breadth, length):
        self.starting_point = starting_point
        self.breadth = breadth
        self.length = length
        self.end_point_x = None
        self.end_point_y = None

    def area(self):
        return self.breadth * self.length

    def calc_end_points(self):
        self.end_point_x = self.starting_point.coordX + self.breadth
        self.end_point_y = self.starting_point.coordY + self.length

    def print_points(self):
        print('Starting Point (X)): ' + str(self.starting_point.coordX))
        print('Starting Point (Y)): ' + str(self.starting_point.coordY))
        print('End Point X-Axis (Top Right): ' + str(self.end_point_x))
        print('End Point Y-Axis (Bottom Left): ' + str(self.end_point_y))


def build_rectangle():
    starting_point = Point(50, 100)
    rect = Rectangle(starting_point=starting_point, breadth=90, length=10)

    return rect


my_rect = build_rectangle()

print(my_rect.area())
my_rect.calc_end_points()
my_rect.print_points()