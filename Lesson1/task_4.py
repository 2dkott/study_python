def check_input():
    try:
        ax = int(input("Введите X для координаты А: "))
        ay = int(input("Введите Y для координаты А: "))
        bx = int(input("Введите X для координаты B: "))
        by = int(input("Введите Y для координаты B: "))
        return (ax, ay), (bx, by)
    except ValueError:
        print("Введено не число")


def get_distance(a_point, b_point):
    return ((b_point[0] - a_point[0]) ** 2 + (b_point[1] - a_point[1]) ** 2) ** 0.5


a_point, b_point = check_input()
print("Растояние: " + str(get_distance(a_point, b_point)))
