# Змей, [09.06.2022 21:47]
# [Forwarded from sept-2021-python]
# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:
#
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 21, 22, 23, 24,25]


def list_packer(lst: list) -> list:
    list_return = []
    list_inner = []
    linked_range = 1
    while True:
        if not lst:
            break
        if len(lst) < linked_range:
            list_return.append(lst)
            break
        for i in range(linked_range):
            list_inner.append(lst.pop(0))
        list_return.append(list_inner.copy())
        list_inner.clear()
        linked_range += 1

    return list_return


print(list_packer(my_list))
