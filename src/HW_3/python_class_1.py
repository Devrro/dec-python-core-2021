# Змей, [14.06.2022 21:48]
# #ДЗ
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return self.x * self.y

    def __add__(self, other):
        return self.square() + other.square()

    def __sub__(self, other):
        return self.square() - other.square()

    def __eq__(self, other):
        return self.square() == other.square()

    def __ne__(self, other):
        return self.square() != other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __len__(self):
        return self.x * 2 + self.y * 2

    def __str__(self):
        return f'x = {self.x} y = {self.y}'

    def __repr__(self):
        return self.__str__()


rec1 = Rectangle(7, 5)
rec2 = Rectangle(3, 100)
print(rec1 != rec2)
print(rec1)
print(rec2)