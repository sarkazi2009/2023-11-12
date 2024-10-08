
import math


class Figure:
    sides_count = 0

    def __init__(self, __color: tuple[int, int, int], *__sides, filled=False):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_sides(self, *sides):
        if len(sides) < self.sides_count:
            return False
        for side in sides:
            if side < 1:
                return False
        return True

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color: tuple[int, int, int], __sides, filled=False):
        super().__init__(__color, __sides, filled=filled)
        self.__radius = __sides / (2 * math.pi)

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color: tuple[int, int, int], *__sides, filled=False):
        super().__init__(__color, __sides, filled=filled)

    def get_square(self):
        p = sum(self.__sides) / 2
        return math.sqrt(p * (p - __sides[0]) * (p - __sides[1]) * (p - __sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color: tuple[int, int, int], __sides, filled=False):
        cube_sides = [__sides] * self.sides_count
        super().__init__(__color, *cube_sides, filled=filled)




    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

