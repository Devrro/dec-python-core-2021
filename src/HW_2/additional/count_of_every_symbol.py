# Змей, [09.06.2022 21: 47]
# [Forwarded
# from sept
# #
# # -2021 - python]
# # прога, що
# # виводить
# # кількість
# # кожного
# # символа
# # з
# # введеної
# # строки,
# # наприклад:
# # st = 'as 23 fdfdg544'  # введена строка
# #
# # 'a' -> 1  # вивело в консолі
# # 's' -> 1
# # ' ' -> 2
# # '2' -> 1
# # '3' -> 1
# # 'f' -> 2
# # 'd' -> 2
# # 'g' -> 1
# # '5' -> 1
# # '4' -> 2


def count_elems() -> dict:
    string = input('Enter your string: ')
    lst = list(string)
    count_elem = {}
    for i in lst:
        count_elem[i] = count_elem.get(i, 0) + 1
    for i in count_elem.keys():
        print(f"'{i}' -> {count_elem[i]}")
    return count_elem


st = 'as 23 fdfdg544'

count_elems()
