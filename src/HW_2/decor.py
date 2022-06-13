# Змей, [09.06.2022 21:45]
# создать декоратор который будет считать сколько раз была запущена функция и будет выводит это значение после каждого запуска функции
from typing import Callable


def decor(func) -> Callable[[str], None]:
    counter = 0

    def inside(*args, **kwargs) -> None:
        nonlocal counter
        counter += 1
        print(counter)
        func(*args, **kwargs)
        print('--------------------------')

    return inside


@decor
def counter_log(st):
    print(st)


counter_log('he')
counter_log('nope')
counter_log('he')
