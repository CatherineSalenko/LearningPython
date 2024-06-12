
""" lesson 7
7. Функциональное программирование
"""
import mydefs


def ex_1():
    """
    1. Дан список чисел. С помощью map() получить список, где
    каждое число из исходного списка переведено в строку.
    Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]
    """

    numbers = [1, 2, 3]
    print(list(map(str, numbers)))


def ex_2():
    """
    2. Дан список чисел. С помощью filter() получить список тех
    элементов из исходного списка, значение которых больше 0.
    """

    numbers = [-2, -1, 0, 1, 2, 3]
    print(list(filter(lambda x: x > 0, numbers)))


def ex_3():
    """
    3. Дан список строк. С помощью filter() получить список тех
строк из исходного списка, которые являются палиндромами
(читаются в обе стороны одинаково, например, ’abcсba’)
    """

    strings = ['abc', 'level', 'radar', 'hello', 'world', 'madam']
    print(list(filter(lambda s: s == s[::-1], strings)))


def ex_4():
    """
    4. Сделать декоратор, который измеряет время, затраченное
    на выполнение декорируемой функции
    """

    result = mydefs.example_function(100)
    print(f"Result: {result}")


def ex_5():
    """
    5. Используя map() и reduce() посчитать площадь квартиры,
    имея на входе характеристики комнат квартиры. Пример входных
    данных:
    rooms = [
    {"name": ”Kitchen", "length": 6, "width": 4},
    {"name": ”Room 1", "length": 5.5, "width": 4.5},
    {"name": ”Room 2", "length": 5, "width": 4},
    {"name": ”Room 3", "length": 7, "width": 6.3},]
    """
    rooms = [
        {"name": "Kitchen", "length": 6, "width": 4},
        {"name": "Room 1", "length": 5.5, "width": 4.5},
        {"name": "Room 2", "length": 5, "width": 4},
        {"name": "Room 3", "length": 7, "width": 6.3},
    ]
    total_area = mydefs.calculate_total_area(rooms)
    print(f"Total area of the apartment: {total_area} square units")




