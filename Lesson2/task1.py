def check_input():
    try:
        return float(input("Введите число: "))
    except ValueError:
        print("Введено не число")


def get_sum_of_all_numbers(float_number):
    total_sum = 0
    numbers_only = str(float_number).replace(".", "")
    for x in numbers_only:
        total_sum = total_sum + int(x)
    return total_sum


print("Сумма: " + str(get_sum_of_all_numbers(check_input())))
