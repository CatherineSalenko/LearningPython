
"""
Основы Python (часть 3)
"""


import math
import mydefs

def ex_1():
    print("не делаем ")


def ex_2():
    """ 2ex
    2. Маша хочет накопить на телефон, который стоит N денег. Маша
    может откладывать k рублей каждый день, кроме воскресенья (в
    воскресенье она тратит эти деньги на поход в кино). Маша начинает
    копить в понедельник. За сколько дней она накопит нужную сумму?
    """

    phone_price = int(input("write phone price "))
    cash = int(input("write how mach many Marry can save every day "))
    cinema_price = int(input("write how much many Marry spand on cinema on Sunday "))

    save_many = 0
    count_days = 1
    while save_many != phone_price:
        if count_days % 7 != 0:
            save_many = save_many + cash
        else:
            save_many = save_many - cinema_price

        count_days = count_days + 1

    print("Marry need " + str(count_days) + " for buy new phone")


def ex_3():
    """
    3. Реализовать вывод последовательности чисел Фибоначчи (1 1 2
    3 5 8 13 21 34 55 89 ...), где каждое следующее число является
    суммой двух предыдущих.
    """

    i = 0
    count_number = input("write count number")
    mass = [1, 1]
    while i <= count_number:
        last_number = mass[-1]
        befor_last_number = mass[-2]
        result = last_number + befor_last_number
        mass.append(result)
        i += 1
    print(mass)


def ex_4():
    """
    4. Дан список чисел. Реализовать программу, которая посчитает
    сумму всех чисел в списке, а также найдет минимальный и
    максимальный элементы
    """

    list_size = int(input("write list size "))
    i = 1
    summ = 0
    mass = []
    while i <= list_size:
        your_number = float(input("write your number №" + str(i) + " "))
        mass.append(your_number)
        summ += your_number
        i += 1

    print("your list ")
    print(mass)
    print("summa all number is " + str(summ))
    print("max " + str(max(mass)))
    print("min " + str(min(mass)))


def ex_5():
    """
    5. Дан список чисел. Реализовать программу, которая проверит, все
    ли числа в списке уникальны (встречаются только один раз).
    Программа должна вывести результат проверки, и, если не все
    элементы уникальны, вывести дублирующиеся элементы и
    количество их повторений в списке
    """

    list_size = int(input("write list size "))
    i = 1
    mass = []
    deplicate_list = []
    while i <= list_size:
        your_number = float(input("write your number №" + str(i) + " "))

        if your_number in mass:
            if your_number in deplicate_list:
                print("you write it again")
            else:
                deplicate_list.append(your_number)

        mass.append(your_number)
        i += 1

    print("your list")
    print(mass)
    print("deplicate:")

    for i in deplicate_list:
        print("number  " + str(i) + " count " + str(mass.count(i)))


def ex_6():
    """
    6. Дан список чисел, отсортированных по возрастанию. На вход
    принимается значение, равное одному из элементов списка.
    Реализовать алгоритм бинарного поиска, на выходе программа
    должна вывести позицию искомого элемента в исходном списке
    """

    mass = mydefs.create_sort_mass()
    print(mass)

    find_number = int(input("write find number "))

    check_number = 0
    left_border_index = 0
    rights_border_index = len(mass)
    central_index = len(mass) // 2

    while check_number != find_number and left_border_index <= rights_border_index:

        check_number = mass[central_index]
        if check_number > find_number:
            rights_border_index -= 1
        elif check_number < find_number:
            left_border_index += 1

        central_index = (left_border_index + rights_border_index) // 2

    if left_border_index > rights_border_index:
        print('No value')
    else:
        print('index =', central_index)


