# 2) для хранения и чтения данных использовать файлы
#
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты

import json
from difflib import SequenceMatcher

number_of_options = [
    '1)Створити запис',
    '2)Список всіх записів',
    '3)Загальна сума покупок',
    '4)Найдорожча покупка',
    '5)Пошук за назвою покупки',
    '6)Видалити всі записи',
    '7)Вихід',
]


def p_menu(num_options) -> int:
    print(*num_options, sep='\n')
    while True:
        num = int(input('Введіть ваш вибір'))
        if 0 < num <= len(num_options):
            break
        else:
            print('Неправильний ввід')
    return num


def create_note(lst):
    note = input('Введіть назву вашої покупки: ')
    price = int(input('Введіть вартість покупки'))
    lst.append({'note': note, 'price': price})


def get_sum(lst: [{}, ...]) -> int:
    list_sum = 0
    for i in lst:
        list_sum += i['price']
    return list_sum


def get_highest_by_price(lst: [{}, ...]) -> {}:
    note, price = (max(lst, key=lambda x: x['price'])).values()
    return note, price


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def get_search_value(lst: [{}, ...]):
    search = 'val 5'
    note, price = max(lst, key=lambda x: similar(search, x["note"])).values()
    return note, price


def erase_all_data() -> bool:
    print("Ви точно хочете очистити список?")
    answer = input('Введіть Y, щоб очистити файл: ');
    if answer == 'Y':
        return True


def shopping_list(opt, file_name='shopping_list.txt'):
    body_shop_list: list[{}, ...] = []
    with open(file_name, 'r+') as shp_lst:
        if shp_lst:
            try:
                body_shop_list = json.load(shp_lst)
            except Exception as err:
                print(err)
    while True:
        choice = p_menu(opt)
        match choice:
            case 1:
                create_note(body_shop_list)
            case 2:
                # Тут потім додати функцію, яка нормально виводитиме список
                print(body_shop_list)
            case 3:
                print(get_sum(body_shop_list))
            case 4:
                note, price = get_highest_by_price(body_shop_list)
                print("Товар: " + note, "Ціна: " + str(price))
            case 5:
                note, price = get_search_value(body_shop_list)
                print("Товар: " + note, "Ціна: " + str(price))
            case 6:
                if erase_all_data():
                    body_shop_list.clear()
                    open(file_name, 'w').close()
            case 7:
                with open(file_name, 'r+') as shp_lst:
                    shp_lst.write(json.dumps(body_shop_list))
                break
        input('Натисність будь-яку клавішу, щоб продовжити')


# shp_lst.write(json.dumps([{'hello': '1'}]))

shopping_list(opt=number_of_options)
