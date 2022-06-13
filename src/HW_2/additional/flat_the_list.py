#
# Вирівняти багаторівневий масив в однорівневий
#     [1,3, ['Hello, 'Word', [9,6,1]], ['oops'], 9] -> [1, 3, 'Hello, 'Word', 9, 6, 1, 'oops', 9]
# flat використовувати заборонено.
#
my_list = [1, 3, ['Hello', 'Word', [9, 6, 1]], ['oops'], ['asdasd', ['space', ['inner', ['hello']]]], 9]


def flatter(lst: list) -> list:
    for index, elem in enumerate(lst):
        if type(elem) == list:
            temp = elem
            lst.remove(lst[index])
            for j in range(len(temp)):
                lst.insert(index + j, elem[j])
    while any(map(lambda x: isinstance(x, list), lst)):
        flatter(lst)
    return lst


print(flatter(my_list))
