# Используем функцию summer из предыдущего примера.
# Её немного изменили, но могли появиться и новые ошибки.
#
# В данном задании Вам необходимо написать параметризованный тест 
# состоящий из одной функции, используя библиотеку pytest.
#
# В текущем примере функции утверждения о работе функции 
#
# Изначально функция summer была задумана следующим образом:
#    1.Функция складывает позиционные аргументы 
#      и возвращает правильный ответ если передано 
#      более двух аргументов.
#      summer(3,6,9) == 18
#    2.Функция возвращает ответ "Большое число" если
#      сумма переданных аргументов превышает 300.
#      summer(301, 25) == "Большое число"
#    3.Функция возвращает ответ "Мало аргументов"
#      Если передан только один аргумент.
#      summer(301) == "Мало аргументов"
#      - Реализуйте проверку в функции test_many
#    4.Функция возвращает ответ "ОШИБКА"
#      Если в аргументах передано не целое число.
#      summer("qwe") == "ОШИБКА"
#
#
import os

import pytest


def summer(*args):
    if len(args) == 1:
        return "Мало аргументов"
    for arg in args:
        if not isinstance(arg, int):
            return "ОШИБКА"
    if sum(args) > 300:
        return "Большое число"
    return sum(args)


summer_args = [
    [(3, 6, 9), 18],
    [(299, 25), "Большое число"],
    [(301,), "Мало аргументов"],
    [("qwe", 1), "ОШИБКА"]
]


@pytest.mark.parametrize('test_input, expected', summer_args)
def test_sum_numbers(test_input, expected):
    assert summer(*test_input) == expected


if __name__ == "__main__":
    os.system("pytest")
