"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import time

def half_division_predict(number: int = 1) -> int:
    """Угадываем число методом половинного деления

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    lo_level = 1 # нижняя граница интервала
    hi_level = 101 # верхняя граница интервала
    predict_number = (lo_level + hi_level) // 2 # делим интервал возожных значений пополам

    while number != predict_number:
        if predict_number > number: hi_level = predict_number
        else: lo_level = predict_number
        predict_number = (lo_level + hi_level) // 2
        count += 1
    return count

def random_division_predict(number: int = 1) -> int:
    """Угадываем число методом случайного деления

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    lo_level = 1 # нижняя граница интервала
    hi_level = 101 # верхняя граница интервала
    predict_number = (lo_level + hi_level) // 2 # делим интервал возожных значений пополам

    while number != predict_number:
        if predict_number > number: hi_level = predict_number
        else: lo_level = predict_number
        predict_number = np.random.randint(lo_level, hi_level+1)
        count += 1
    return count

def by_category_predict(number: int = 1) -> int:
    """Угадываем число методом поиска по разрядаум -
    сначала находим десятки потом единицы числа
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    tens = 5 # десятки
    units = 5 # единицы
    predict_number = tens * 10 + units

    while number // 10 != tens:
        if tens > number // 10: tens -= 1
        else: tens += 1
        count += 1

    while number % 10 != units:
        if units > number % 10: units -= 1
        else: units += 1
        count += 1

    return count

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(predict_func) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    size = 1000
    count_ls = []
    np.random.seed(42)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(size))  # загадали список чисел

    start_time = time.time()
    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Алгоритм находит число в среднем за {score} итераций. {round((time.time() - start_time), 5)} секунд на {size} наблюдений")
    return


if __name__ == "__main__":
    # RUN
    print("="*50)
    print("*** Алгоритм случайного угадывания ***")
    score_game(random_predict)
    print("="*50)
    print("*** Алгоритм случайного деления ***")
    score_game(random_division_predict)
    print("="*50)
    print("*** Алгоритм поиска по разрядам ***")
    score_game(by_category_predict)
    print("="*50)
    print("*** Алгоритм половинного деления ***")
    score_game(half_division_predict)
    print("="*50)
