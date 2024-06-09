"""
Структурное программирование
"""

import mydefs


def ex_1():
    """
    1. Дан список чисел, отсортированных по возрастанию. На
    вход принимается значение, равное одному из элементов списка.
    Реализовать функцию, выполняющую рекурсивный алгоритм
    бинарного поиска, на выходе программа должна вывести позицию
    искомого элемента в исходном списке
    """
    mass = mydefs.create_sort_mass()
    find_number = int(input("write find number "))

    check_number = 0
    left_border_index = 0
    rights_border_index = len(mass)
    central_index = len(mass) // 2

    mydefs.binary_search(mass, check_number, find_number, left_border_index, rights_border_index, central_index)


def ex_2():
    """
     2. Программа получает на вход число в десятичной системе
    счисления. Реализовать функцию, которая переводит входное
    число в двоичную систему счисления. Допускается реализация
    функции как в рекурсивном варианте, так и с итеративным
    подходом.
    """
    your_number = input("write your number ")
    bin_number = bin(your_number)
    print(bin_number)


def ex_3():
    """
    3. Программа получает на вход число. Реализовать функцию,
    которая определяет, является ли это число простым (делится
    только на единицу и на само себя).
    """

    your_number = input("write your number ")
    mydefs.simple_number(your_number)


def ex_4():
    """
    4. Программа получает на вход два числа и находит их НОД
    (наибольший общий делитель). Пример: на вход подаются числа 12
    и 18, их НОД равен 6
    """

    x = input("write first number")
    y = input("write second number")

    mydefs.gcd(x, y)


def ex_5():
    """
    5. Программа получает на вход строку – сообщение и
    указание, что нужно сделать: шифровать или дешифровать.
    Реализовать две функции: первая шифрует заданное сообщение
    шифром Цезаря, вторая – расшифровывает. В зависимости от
    выбора пользователя (шифровать или дешифровать) вызывается
    соответствующая функция, результат выводится в консоль.
    """

    action = input("Введите действие (шифровать/дешифровать): ").strip().lower()
    message = input("Введите сообщение: ").strip()
    shift = int(input("Введите сдвиг (целое число): ").strip())

    if action == "шифровать":
        result = mydefs.caesar_cipher_encrypt(message, shift)
    elif action == "дешифровать":
        result = mydefs.caesar_cipher_decrypt(message, shift)
    else:
        print("Некорректное действие. Пожалуйста, введите 'шифровать' или 'дешифровать'.")
        return

    print(f"Результат: {result}")


def ex_6():
    """
    6*. См. предыдущую задачу, но вместо шифра Цезаря
    использовать шифр Виженера
    """

    action = input("Введите действие (шифровать/дешифровать): ").strip().lower()
    message = input("Введите сообщение: ").strip()
    key = input("Введите ключ: ").strip()

    if action == "шифровать":
        result = mydefs.vigenere_cipher_encrypt(message, key)
    elif action == "дешифровать":
        result = mydefs.vigenere_cipher_decrypt(message, key)
    else:
        print("Некорректное действие. Пожалуйста, введите 'шифровать' или 'дешифровать'.")
        return

    print(f"Результат: {result}")


def ex_7():
    """
    7. Реализовать функцию, которая создаёт матрицу размером
    M строк на N столбцов и заполняет её рандомными числами
    """

    M = input("введите количество строк")  # Количество строк
    N = input("введите количество столбцов")    # Количество столбцов

    matrix = mydefs.create_random_matrix(M, N, 0, 100)

    return matrix


def ex_8():
    """
    8. Реализовать функцию, которая находит минимальный и
    максимальный элементы в матрице (матрица M x N). Вывести в
    консоль индексы найденных элементов
    """

    matrix = ex_7()
    mydefs.find_min_max(matrix)


def ex_9():
    """
    9. Реализовать функцию, которая находит сумму элементов
    матрицы (матрица M x N). Определить, какую долю в общей сумме
    (процент) составляет сумма элементов каждого столбца
    """

    matrix = ex_7()
    mydefs.calculate_column_percentage(matrix)


def ex_10():
    """
    10*. Реализовать функцию, которая перемножает элементы
    каждого столбца матрицы с соответствующими элементами K-го
    столбца (матрица M x N)
    """

    matrix = ex_7()
    k = input("введите номер столбца")
    mydefs.multiply_columns_with_k(matrix, k)


def ex_11():
    """
    11*. Реализовать функцию, которая суммирует элементы
    каждой строки матрицы с соответствующими элементами L-й строки
    (матрица M x N)
    """

    matrix = ex_7()
    lstr = input("введите номер строки")
    mydefs.sum_rows_with_l(matrix, lstr)


def ex_12():
    """
    12. Программа получает на вход число H. Реализовать
    функцию, которая определяет, какие столбцы имеют хотя бы одно
    такое же число, а какие не имеют (матрица M x N)
    """

    matrix = ex_7()
    H_number = input("введите номер столбца")
    mydefs.columns_with_value(matrix, H_number)


def ex_13():
    """
    13. Реализовать функцию, которая находит сумму элементов
    на главной диагонали и сумму элементов на побочной диагонали
    (матрица M x N)
    """

    matrix = ex_7()
    mydefs.diagonal_sums(matrix)


def ex_14():
    """
    14. Дана матрица M x N. Исходная матрица состоит из нулей и
    единиц. Реализовать функцию, которая добавит к матрице ещё
    один столбец, элементы которого делает количество единиц в
    соответствующей строке чётным
    """
    matrix = [
        [0, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 1]
    ]
    mydefs.add_parity_column(matrix)

