import math


def square(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area


num_side = int(input("Сторона квадрата равна: "))
print(f"Площадь квадрата равна: {square(num_side)}")
