#  Знайти найбільший елемент в масиві за допомогою reduce
#      [1,6,9,0,17,88,4,7] -> 88
import functools

my_list = [1, 6, 9, 0, 17, 88, 4, 7]


def max_by_reduce(lst: list) -> int:
    return functools.reduce(lambda x, y: x if x > y else y, lst)


print(max_by_reduce(my_list))
