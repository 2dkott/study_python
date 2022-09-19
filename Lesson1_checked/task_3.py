def check_input():
    try:
        x = int(input("Введите x: "))
        y = int(input("Введите y: "))
        z = int(input("Введите z: "))
        return x, y, z
    except ValueError:
        print("Введено не число")


def check_statement(xyz):
    left_part = not (xyz[0] or xyz[1] or xyz[2])
    right_part = not xyz[0] and not xyz[1] and not xyz[2]
    return left_part == right_part


values = check_input()

if check_statement(values):
    print(f"True")
else:
    print(f"False")
