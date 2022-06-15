# Змей, [14.06.2022 21:48]
# ДЗ
# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        self.inc_count()

    def __str__(self):
        return f"\n Her name is {self.name} Her age is {self.age} Foot size: {self.foot_size} \n"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def inc_count(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


class Prince(Human):
    def __init__(self, name, age, pr_shoe_size):
        super().__init__(name, age)
        self.pr_shoe_size = pr_shoe_size

    def get_the_chosen_one(self, lst: list[Cinderella]):

        for i in lst:
            if i.foot_size == self.pr_shoe_size:
                print(f'ITS {i.name}! SHE IS THE ONE, BOIII!')
                return i.name


mery, fiona, lida, anna = [
    Cinderella('Mery', 22, 31),
    Cinderella('Fiona', 22, 45),
    Cinderella('Lida', 22, 30),
    Cinderella('Anna', 22, 27)
]

princesses = [
    mery, fiona, lida, anna
]
Charles = Prince('Charles', 26, 27)
print(princesses)
Charles.get_the_chosen_one(princesses)
