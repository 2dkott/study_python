def check_input():
    try:
        return int(input("Введите число: "))
    except ValueError:
        print("Введено не число")


def check_week_end(day_number):

    if day_number in (6, 7):
        print("Этот день выходной")
    elif day_number in (1, 5):
        print("Этот день не выходной")

    print("Введенное число некорректное. Число должно быть больше 0 или меньше 8")

check_week_end(check_input())
