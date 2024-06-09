
import math
import random

def create_sort_mass():
    list_size = int(input("write list size "))
    i = 1
    mass = []
    while i <= list_size:
        your_number = int(input("write your number №" + str(i) + " "))
        mass.append(your_number)
        i += 1

    print("your list")
    mass.sort()
    print(mass)
    return mass


def binary_search(mass, check_number, find_number, left_border_index, rights_border_index, central_index):

    if check_number != find_number and left_border_index <= rights_border_index:

        check_number = mass[central_index]
        if check_number > find_number:
            rights_border_index -= 1
        elif check_number < find_number:
            left_border_index += 1

        central_index = (left_border_index + rights_border_index) // 2
        binary_search(mass, check_number, find_number, left_border_index, rights_border_index, central_index)
    else:
        print('index =', central_index)


def simple_number(number):

    k = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k = k + 1
        if k <= 0:
            print("is simple")
        else:
            print("is not simple")


def gcd(a, b):
    """
    Функция для вычисления наибольшего общего делителя (НОД) двух чисел
    с использованием встроенной функции math.gcd.
    """
    print("gcd is ", math.gcd(a, b))


def caesar_cipher_encrypt(message, shift):
    """
    Функция для шифрования сообщения с использованием шифра Цезаря.
    Если символ является буквой, определяется его база сдвига:
    'A' для заглавных букв и 'a' для строчных.
    Вычисляется новый символ с учетом сдвига и добавляется к зашифрованному сообщению.
    Если символ не является буквой,
    он добавляется к зашифрованному сообщению без изменений.
    """

    encrypted_message = ""

    for char in message:
        if char.isalpha():
            shift_base = 'A' if char.isupper() else 'a'
            encrypted_message += chr((ord(char) - ord(shift_base) + shift) % 26 + ord(shift_base))
        else:
            encrypted_message += char
    return encrypted_message


def caesar_cipher_decrypt(message, shift):
    """
    Функция для дешифрования сообщения с использованием шифра Цезаря.
    Используется та же функция шифрования, но со сдвигом в противоположном направлении (отрицательное значение сдвига).
    """
    return caesar_cipher_encrypt(message, -shift)


def vigenere_cipher_encrypt(message, key):
    """
    Функция для шифрования сообщения с использованием шифра Виженера.
    Для каждого символа сообщения, если это буква, вычисляем сдвиг, основанный на соответствующем символе ключа.
    Если символ не является буквой, он добавляется к результату без изменений.
    """
    encrypted_message = ""
    key_length = len(key)
    key_index = 0

    for char in message:
        if char.isalpha():
            shift_base = 'A' if char.isupper() else 'a'
            shift = ord(key[key_index % key_length].upper()) - ord('A')
            encrypted_char = chr((ord(char) - ord(shift_base) + shift) % 26 + ord(shift_base))
            encrypted_message += encrypted_char
            key_index += 1
        else:
            encrypted_message += char

    return encrypted_message


def vigenere_cipher_decrypt(message, key):
    """
    Функция для дешифрования сообщения с использованием шифра Виженера.
    Тоже самое  но с вычитанием сдвиг ключа из символа сообщения.
    """
    decrypted_message = ""
    key_length = len(key)
    key_index = 0

    for char in message:
        if char.isalpha():
            shift_base = 'A' if char.isupper() else 'a'
            shift = ord(key[key_index % key_length].upper()) - ord('A')
            decrypted_char = chr((ord(char) - ord(shift_base) - shift + 26) % 26 + ord(shift_base))
            decrypted_message += decrypted_char
            key_index += 1
        else:
            decrypted_message += char

    return decrypted_message


def create_random_matrix(M, N, min_val=0, max_val=100):

    matrix = [[random.randint(min_val, max_val) for _ in range(N)] for _ in range(M)]
    return matrix


def find_min_max(matrix):

    min_value = max_value = matrix[0][0]
    min_index = max_index = (0, 0)

    # enumerate возвращает  индекс
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value < min_value:
                min_value = value
                min_index = (i, j)
            if value > max_value:
                max_value = value
                max_index = (i, j)

    print(f"Минимальное значение: {min_value} с индексами {min_index}")
    print(f"Максимальное значение: {max_value} с индексами {max_index}")

    return (min_value, min_index), (max_value, max_index)


def calculate_column_percentage(matrix):
    """
    Функция для нахождения суммы элементов матрицы и вычисления доли
    суммы каждого столбца в общей сумме (в процентах).
    """
    num_cols = len(matrix[0])

    # Вычисление общей суммы элементов матрицы
    total_sum = 0
    column_sums = [0] * num_cols

    for row in matrix:
        total_sum += sum(row)
        for j in range(num_cols):
            column_sums[j] += row[j]


    # Вычисление процентного вклада каждого столбца
    column_percentages = [(col_sum / total_sum) * 100 for col_sum in column_sums]

    print(f"Общая сумма элементов матрицы: {total_sum}")
    for col_index, percentage in enumerate(column_percentages):
        print(f"Столбец {col_index + 1}: {percentage:.2f}% от общей суммы")


def multiply_columns_with_k(matrix, k):
    """
    Функция перемножает элементы каждого столбца матрицы с соответствующими элементами K-го столбца.
    """

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Проверка, что индекс столбца k в пределах допустимого диапазона
    if k < 0 or k >= num_cols:
        raise IndexError("Индекс столбца K вне допустимого диапазона")

    # Создание новой матрицы для хранения результатов
    result_matrix = [[0] * num_cols for _ in range(num_rows)]

    # Перемножение элементов
    for i in range(num_rows):
        for j in range(num_cols):
            result_matrix[i][j] = matrix[i][j] * matrix[i][k]

    print(result_matrix)

    for row in result_matrix:
        print(row)


def sum_rows_with_l(matrix, l):
    """
    Функция суммирует элементы каждой строки матрицы с соответствующими элементами L-й строки.
    """

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Проверка, что индекс строки l в пределах допустимого диапазона
    if l < 0 or l >= num_rows:
        raise IndexError("Индекс строки L вне допустимого диапазона")

    # Создание новой матрицы для хранения результатов
    result_matrix = [[0] * num_cols for _ in range(num_rows)]

    # Суммирование элементов
    for i in range(num_rows):
        for j in range(num_cols):
            result_matrix[i][j] = matrix[i][j] + matrix[l][j]

    print(result_matrix)

    for row in result_matrix:
        print(row)



def columns_with_value(matrix, H):
    """
    Функция определяет, какие столбцы матрицы имеют хотя бы одно значение H, а какие не имеют.
    """
    num_cols = len(matrix[0])

    # Инициализация списков для хранения индексов столбцов
    cols_with_H = []
    cols_without_H = []

    # Проверка каждого столбца
    for j in range(num_cols):
        has_H = False
        for row in matrix:
            if row[j] == H:
                has_H = True
                break
        if has_H:
            cols_with_H.append(j)
        else:
            cols_without_H.append(j)

    print(f"Столбцы с числом {H}: {cols_with_H}")
    print(f"Столбцы без числа {H}: {cols_without_H}")


def diagonal_sums(matrix):
    """
    Функция находит сумму элементов на главной диагонали и сумму элементов на побочной диагонали.
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Проверка, что матрица квадратная
    if num_rows != num_cols:
        raise ValueError("Матрица должна быть квадратной")

    main_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(num_rows):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][num_cols - 1 - i]

    print(f"Сумма главной диагонали: {main_diagonal_sum}")
    print(f"Сумма побочной диагонали: {secondary_diagonal_sum}")


def add_parity_column(matrix):
    """
    Функция добавляет к матрице столбец, элементы которого делают количество единиц в соответствующей строке чётным.
    """
    new_matrix = []

    for row in matrix:
        # Подсчёт количества единиц в строке
        count_ones = sum(row)
        # Определение значения для нового столбца
        parity_value = 0 if count_ones % 2 == 0 else 1
        # Добавление нового столбца к строке
        new_row = row + [parity_value]
        new_matrix.append(new_row)

    for row in new_matrix:
        print(row)
