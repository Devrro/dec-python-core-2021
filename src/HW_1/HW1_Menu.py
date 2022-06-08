# 4) переделать первое задание под меню с помощью цикла
def run_menu():
    lst = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

    while True:
        print('1.Find min number in list')
        print('2.Remove duplicates in list')
        print('3.Replace element of list')
        print('4.Exit')
        enter = int(input('Choose your option:'))
        if enter == 1:
            print(min(lst))
        elif enter == 2:
            lst = (list(set(lst)))
            print(lst)
        elif enter == 3:
            for i, e in enumerate(lst):
                if i % 4 == 0 and i != 0:
                    lst[i] = 'X'
            print(lst)
        if enter == 4:
            return


run_menu()
