
""" lesson4
Основы Python (часть 2)
"""


import math
from math import cos, sin


def ex_1():
    """
    Используя модуль math, вычислите значения по формулам.
    Значения a, b, x ввести с клавиатуры, вывести 4 рассчитанных по
    формулам значения. Сделать красиво оформленные ввод и вывод
    данных
    """

    a = float(input("write a"))
    b = float(input("write b"))
    first_y = (((pow(a, 2))/3) + ((pow(a, 2) + 4)/b) + ((math.sqrt(pow(a,2) + 4))/4) +
               ((math.sqrt(pow((pow(a, 2) + 4), 3)))/4))

    x = float(input("write x"))

    second_y = math.sqrt((pow(cos(pow(x, 2)), 2) + pow(sin(2*x-1), 2)), 3)
    third_y = cos(x) + sin(x)
    forth_y = (5*x) + 3*(pow(x, 2)) * math.sqrt(1 + pow(sin(x)))

    print(second_y)
    print(third_y)
    print(forth_y)


def ex_2():
    """
    2. «Играл с кредитами – проиграл»
    m – ежемесячная выплата
    i – годовая процентная ставка
    p – месячная процентная ставка
    s – сумма займа
    n – количество месяцев, на которые взят кредит
    Пользователь вводит с клавиатуры i, s и n, программа должна рассчитать размер
    ежемесячной выплаты по формуле, а также найти, сколько пользователь всего
    заплатит банку и сколько составит переплата.
    Сделать ввод/вывод данных красивым интерактивом
    """

    print("i - годовая процентная ставка")
    i = float(input("write i"))
    print("s - сумма займа")
    s = float(input("write s"))
    print("n - количество месяцев, на которые взят кредит")
    n = float(input("write n"))
    # p – месячная процентная ставка
    p = i/12

    m = ((s * p) * pow((1 + p), n))/ pow((1 + p), n) - 1
    all_credit_summ = m * n
    bank_take = all_credit_summ - s
    print("result")
    print("you take " + s)
    print("you need pay every month " + m)
    print("all credit summ " + all_credit_summ)
    print("bank will receive " + bank_take)


def planet_years(R, V):
    pi = 3.14
    result_l = ((2 * R * pi) / V)
    return result_l


def ex_3():
    """
    3. «Интерстеллар»
    L - длина года на планете
    R – радиус орбиты планеты (млн. км.)
    𝑣 – орбитальная скорость (км/ч)

    Пользователь вводит с клавиатуры информацию о двух планетах: радиус и
    орбитальную скорость. Программа должна посчитать и вывести длину
    года на первой и второй планетах, а также вывести, правда ли,
    что на первой планете год длиннее, чем на второй.
    Сделать ввод/вывод данных красивым интерактивом.
    """

    print("write info about two planet:")
    print("first planet:")
    print("R - радиус орбиты планеты (млн. км.)")
    R1 = float(input("write R:"))
    print("v -орбитальная скорость (км/ч)")
    V1 = float(input("write v:"))

    year1 = planet_years(R1, V1)
    print("1  year on first planet is " + year1)

    print("second planet:")
    print("R - радиус орбиты планеты (млн. км.)")
    R2 = float(input("write R:"))
    print("v -орбитальная скорость (км/ч)")
    V2 = float(input("write v:"))

    year2 = planet_years(R2, V2)
    print("1 year on second planet is " + year2)

    if year1 > year2:
        L1_more = year1 - year2
        print("1 year on planet 1 is more then planet 2 on " + L1_more)
    else:
        L2_more = year2 - year1
        print("1 year on planet 2 is more then planet 1 on " + L2_more)
