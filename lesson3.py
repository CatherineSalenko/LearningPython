
""" lesson 3
Основы Python (часть 1)
"""

import math


def get_summ(first, second, third):
    summ = first + second + third
    return summ


def get_razz(first, second, third):
    razz = first - second - third


def get_proizv(first, second, third):
    proizv = first * second * third
    return proizv


def get_rez_f1(first, second, third):
    rez = (first - second) + third
    return rez


def get_rezalt_f2(first, second, third):
    rez = (first * second) / third
    return rez


def get_rezalt_f3(first, second, third):
    rez = (first + second) % third
    return rez


def ex_1():
    """
    1. Есть три целочисленные переменные, нужно посчитать:
    ● сумму
    ● разность
    ● произведение
    ● от первой переменной отнять вторую и прибавить третью
    ● поделить произведение двух переменных на третью
    ● от суммы первых двух переменных найти остаток от деления
    на третью переменную
    """

    first = int(input("write first number"))
    second = int(input("write second number"))
    third = int(input("write third number"))

    print("summ " + str(get_summ(first, second, third)))
    print("razz " + str(get_razz(first, second, third)))
    print("proizv " + str(get_proizv(first, second, third)))
    print("function 1 " + str(get_rez_f1(first, second, third)))
    print("function 2" + str(get_rezalt_f2(first, second, third)))
    print("function 3" + str(get_rezalt_f3(first, second, third)))


def ex_2():
    """
    2. Дан прямоугольный треугольник с катетами cat_a и cat_b. Найти площадь треугольника и его гипотенузу.
    """

    cat_a = float(input("write cat_a"))
    cat_b = float(input("write cat_b"))
    square = (cat_a * cat_b)/2
    hypotenuse = math.sqrt(pow(cat_a, 2) + pow(cat_b, 2))

    print("square is " + str(square))
    print("hypotenuse is "+ str(hypotenuse))


def ex_3():
    """
    3. Дана строка, состоящая из слов, разделенных пробелами. (Вот 4
    варианта тестовых данных для программы: ‘Hello world’, ‘a b c’, ‘test’,
    ‘test1 test2 test3 test4 test5’). Определите, сколько в ней слов
    """
    str1 = "Hello world"
    str2 = "a b c"
    str3 = "test"
    str4 = "test1 test2 test3 test4 test5"
    print("in line " + str(len(str1.split())) + " words")
    print("in line " + str(len(str2.split())) + " words")
    print("in line " + str(len(str3.split())) + " words")
    print("in line " + str(len(str4.split())) + " words")


def ex_4():
    """
    4. Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
    Подсказка: использовать метод replace с параметрами. Например, дано: ‘hhhabchghhh’, должно быть: ‘hHHabcHgHHh’
    """
    str = "hhhabchghhh"
    str.count("h")
    first_symbol = str[0]
    last_symbol = str[-1]
    center = str[1:-1]
    new_center = center.replace("h", "H")
    new_str = first_symbol + new_center + last_symbol
    print(new_str)


def ex_5():
    """
    5. Дана строка.
    ● Сначала выведите третий символ этой строки.
    ● Во второй строке выведите предпоследний символ строки.
    ● В третьей строке выведите первые пять символов строки.
    ● В четвертой выведите всю до последних двух символов.
    ● В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы
    выводятся начиная с первого).
    ● В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
    ● В седьмой строке выведите все символы в обратном порядке.
    ● В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
    ● В девятой строке выведите длину данной строки.
    Тестовые данные для 5 задачи:
    строка ‘Hello’, должно быть:
    строка ‘TEST-STR’:
    """

    str1 = "Hello"
    str2 = "TEST-STR"

    print(str1[2])
    print(str2[2])
    print(str1[-2])
    print(str2[-2])
    print(str1[:4])
    print(str2[:4])
    print(str1[:-2])
    print(str2[:-2])
    print(str1[::2])
    print(str2[::2])
    print(str1[1::2])
    print(str2[1::2])
    print(str1[::-1])
    print(str2[::-1])
    print(str1[-1::-2])
    print(str2[-1::-2])
    print(len(str1))
    print(len(str2))


def ex_6():
    """
    6. Дано целое число. Выведите его последнюю цифру. Например, дано 200 - последняя цифра 0. Дано 123 - последняя
    цифра 3. Дано 587 - последняя 7
    """
    last_number = input("write number ")
    print(last_number[-1])


def ex_7():
    """
    7. Дано трехзначное число, найти количество его десятков. Например, дано 123 – количество десятков: 2, дано 978 –
    количество десятков: 7
    """
    last_number = input("write number ")
    print(last_number[2])


def ex_8():
    """
    8. Дано трехзначное число, найти сумму его цифр. Например, дано 123 – сумма 6, дано 555, сумма 15.
    """
    number = input("write a number ")
    mass = list(number)
    summ = 0
    for i in mass:
        summ += int(i)

    print(summ)


