# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# - створити функцію яка виводить ліст
def show_list(lst):
    print(lst)


# - створити функцію яка приймає три числа та виводить та повертає найменьше.
def return_lowest(a, b, c):
    print(min(a, b, c))
    return min(a, b, c)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def return_biggest(a, b, c):
    print(max(a, b, c))
    return max(a, b, c)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def return_lowest_and_print_biggest(*args):
    print(max(args))
    return min(args)


# - створити функцію яка повертає найбільше число з ліста
def rt_biggest_list(lst):
    return max(lst)


# - створити функцію яка повертає найменьше число з ліста
def rt_lowest_list(lst):
    return min(lst)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_of_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def avg(lst):
    sum = sum_of_list(lst)
    return sum // len(lst)

