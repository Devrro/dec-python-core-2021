# // Дан массив целых чисел, найдите тот, который встречается нечетное количество раз.
# // Всегда будет только одно целое число, которое встречается нечетное количество раз
# //     [1,2,3,4,5,2,4,1,3] -> 5

lstN = [1, 2, 3, 4, 5, 2, 4, 1, 3]


def count_numbers(lst: list) -> dict:
    number_count = {}
    for i in lst:
        number_count[i] = number_count.get(i, 0) + 1

    return number_count


def count_not_odd(lst: list) -> int:
    number_count = count_numbers(lst)
    for i in number_count.keys():
        if number_count[i] % 2 != 0:
            return i


print(count_not_odd(lstN))
