# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
# Пример:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(number: int) -> str:
    string = []
    string.extend(str(number))
    for i, elem in enumerate(string):
        string[i] = str(int(elem) * (10**(len(string)-1-i)))
    while '0' in string:
        string.remove('0')
    string1 = ' + '.join(string)
    return string1


print(expanded_form(813514))
