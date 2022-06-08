# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

str = input("Enter your string: ")
str1 = []
str1.extend(str)
str1.append('END')
reformat2 = []
num = []
for i in str1:
    if i.isdigit():
        num.append(i)
    else:
        if(num != []):
            reformat2.append(num.copy())
        num.clear()
    # if num:
    #     reformat2.append(num.copy())
str = [''.join(i) for i in reformat2]
print(', '.join(str))