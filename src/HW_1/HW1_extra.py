from tabulate import tabulate
# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - найти min число в листе
#   - удалить все дубликаты в листе
#   - заменить каждое четвертое значение на "Х"
# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# 3) вывести табличку умножения с помощью цикла while
# 4) переделать первое задание под меню с помощью цикла

# 1)Дан лист:
lst = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# - найти min число в листе
print(min(lst))

#   - удалить все дубликаты в листе
lst = (list(set(lst)))
print(lst)

#   - заменить каждое четвертое значение на "Х"
for i, e in enumerate(lst):
    if i % 4 == 0 and i != 0:
        lst[i] = 'X'
print(lst)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой
star_count = 10
print('*' * star_count)
for i in range(star_count - 2):
    print('*' + ' ' * (star_count - 2) + '*')
print('*' * star_count)
# 3) вывести табличку умножения с помощью цикла while
i = 1
math_lst = []
while i < 10:
    math_list_small = []
    # print(' ')
    for j in range(1, 10):
        math_list_small.append(j*i)
        # print(i * j, end=',')
    i += 1
    math_lst.append(math_list_small)
print(math_lst)
for row in math_lst:
    print('{:>1} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(*row))
