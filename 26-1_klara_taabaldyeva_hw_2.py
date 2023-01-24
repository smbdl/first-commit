# 1
class Figure:
    unit = 'cm'

    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.__side_length = side_length
        self.__perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__side_length ** 2

    def calculate_perimeter(self):
        return self.__side_length * 4

    def info(self):
        return f'Square side length: {self.__side_length}cm, perimeter: {self.calculate_perimeter()}cm,' \
               f' area: {self.calculate_area()}cm².'


class Rectangle(Figure):
    def __init__(self, length, width):
        super(Rectangle, self).__init__()
        self.__length = length
        self.__width = width
        self.__perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return (self.__length + self.__width) * 2

    def info(self):
        return f'Rectangle length: {self.__length}cm, width: {self.__width}cm,' \
               f' perimeter: {self.calculate_perimeter()}cm, area: {self.calculate_area()}cm².'


square1 = Square(4)
square2 = Square(5)
rectangle1 = Rectangle(4, 8)
rectangle2 = Rectangle(5, 7)
rectangle3 = Rectangle(6, 9)
list_figures = [square1, square2, rectangle1, rectangle2, rectangle3]
for i in list_figures:
    print(i.info())


# 2
class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.__radius = radius

    def calculate_area(self):
        return round(3.14 * (self.__radius ** 2), 2)

    def info(self):
        return f'Circle radius: {self.__radius}cm, area: {self.calculate_area()}см².'


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return 0.5 * (self.__side_a * self.__side_b)

    def info(self):
        return f'RightTriangle side a: {self.__side_a}cm, side b: {self.__side_b}cm,' \
               f' area : {self.calculate_area()} см².'


circle1 = Circle(5)
circle2 = Circle(10)
circle3 = Circle(15)
right_triangle1 = RightTriangle(6, 8)
right_triangle2 = RightTriangle(8, 12)

figure_list = [circle1, circle2, circle3, right_triangle1, right_triangle2]
for i in figure_list:
    print(i.info())
