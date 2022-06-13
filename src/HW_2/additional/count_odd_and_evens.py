# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3


def count_odd_and_even(number: int) -> str:
    number = list(str(number))
    count = {'even': 0, 'odd': 0}
    for i in number:
        if int(i) % 2 == 0:
            count['even'] += 1
        else:
            count['odd'] += 1
    print("п = " + str(count['even']) + " н = " + str(count['odd']))


count_odd_and_even(22223)
