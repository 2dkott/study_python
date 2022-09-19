import time


def check_input():
    try:
        min = int(input("Введите начало границы для случайного числа: "))
        max = int(input("Введите конец границы для случайного числа: "))
        return min, max
    except ValueError:
        print("Введено не число")


def get_random(min, max):
    range = len(str(max))
    temp = min
    while not max > temp > min:
        temp = int(str(int(time.time() * 1000))[-range])

    return temp


min, max = check_input()

print(f"Случайно число: {get_random(min, max)} между границами от {min} до {max}")
