def check_input():
    try:
        x = int(input("Введите x: "))
        y = int(input("Введите y: "))
        return x, y
    except ValueError:
        print("Введено не число")


def check_area(coordinates):
    area = 4
    if coordinates[0] > 0 and coordinates[1] > 0:
        area = 1
    elif coordinates[0] < 0 and coordinates[1] > 0:
        area = 2
    elif coordinates[0] < 0 and coordinates[1] < 0:
        area = 3
    print(f"Координаты находятся в плоскости {area}")


check_area(check_input())
