# Змей, [15.06.2022 15:56]
# Для тех кому скучно:
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazines()
#     print('-' * 40)
#     # Main.show_all_books()
from __future__ import annotations

from abc import ABC, abstractmethod


class Printable(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def print(*args, **kwargs):
        print(*args, **kwargs)


class Book(Printable):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def print(*args, **kwargs):
        print(*args, **kwargs)


class Magazine(Printable):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def print(*args, **kwargs):
        print(*args, **kwargs)


class Main:

    def __init__(self):
        self.printable_list: list[Book | Magazine] = []

    def add_to_printable_list(self, obj: Book | Magazine):
        self.printable_list.append(obj) if isinstance(obj, (Magazine, Book)) else print('Cant add this object')

    def show_shopping_list(self):
        return self.printable_list

    def show_all_magazines(self):
        return [Printable.print(i) for i in self.printable_list if isinstance(i, Magazine)]

    def show_all_books(self):
        return [Printable.print(i) for i in self.printable_list if isinstance(i, Book)]


shopper = Main()

shopper.add_to_printable_list(Magazine('Magazine1'))
shopper.add_to_printable_list(Book('Book1'))
shopper.add_to_printable_list(Book('Book2'))
shopper.add_to_printable_list(Book('Book3'))
shopper.add_to_printable_list(Magazine('Magazine2'))
print(shopper.show_shopping_list())
shopper.show_all_magazines()
shopper.show_all_books()
