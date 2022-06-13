# Змей, [09.06.2022 21:46]
# сделайте функцию на замыкания которая будет возвращать декоратор который будет считать общее количество запущенных  функций декорированных этим декоратором
from typing import Callable


def make_decorator() -> Callable[[str], Callable]:
    counter = 0

    def decor(func) -> Callable[[any], None]:

        def inside(*args, **kwargs) -> None:
            nonlocal counter
            counter += 1
            print(counter)
            func(*args, **kwargs)
            print('--------------------------')

        return inside
    return decor


decorated = make_decorator()
decorated2 = make_decorator()


@decorated
def counter_log(st):
    print(st)


@decorated
def counter_log2(st):
    print(st)


@decorated2
def counter_log4(st):
    print(st)


@decorated2
def counter_log3(st):
    print(st)


counter_log('he')
counter_log2('nope')
counter_log2('nope')
counter_log('he')
counter_log2('asdasd')
counter_log3('nope')
counter_log4('he')
counter_log3('asdasd')
