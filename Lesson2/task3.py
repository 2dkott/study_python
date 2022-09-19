def check_input():
    try:
        return int(input("Введите число: "))
    except ValueError:
        print("Введено не число")


def get_polyndrom(number):
    polyndrom = 0
    while (number != 0):
        edge_number = number % 10
        polyndrom = polyndrom * 10 + edge_number
        number = int(number / 10)
    return polyndrom


number = check_input()
print("Число: " + str(number) + " полиндром - " + str(get_polyndrom(number)))
