def check_input():
    try:
        return int(input("Введите число: "))
    except ValueError:
        print("Введено не число")


def recur_multiply(number):
    if number == 1:
        return 1

    return number * recur_multiply(number - 1)


def get_list(number_range):
    multiply_list = []

    for x in range(1, number_range):
        multiply_list.append(recur_multiply(x))

    return multiply_list


number = check_input()
print("Число: " + str(number) + " набор произведений: " + str(get_list(number+1)))
