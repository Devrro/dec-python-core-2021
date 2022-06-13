# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все
from typing import Callable


def notebook() -> tuple[Callable[[str], list], ...]:
    todo_list: list = []

    def add_todo(todo: str) -> list:
        todo_list.append(todo)
        return todo_list

    def get_all() -> list:
        return todo_list

    return add_todo, get_all


a_add_todo, a_get_all = notebook()

a_add_todo('work hard')
a_add_todo('cook lunch')
a_add_todo('take shower')
a_add_todo('find you mecha keys')
a_add_todo('free time')

print(a_get_all())
