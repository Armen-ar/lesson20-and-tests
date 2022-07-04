# фаил c тестами № 2
# Основной текст задания находится в файле main_summer_test.py
#
from functools import reduce

# Исходная функция:
import pytest


@pytest.fixture
def incoming_list():
    return [7, "4", 15, "12", 95, 5, 3, 8]


def multiplicator(*args):
    return reduce(lambda x, y: x * y, args)


def test_multiplicator(list_creator):
    multiple_sum = reduce(lambda x, y: x * y, list_creator)
    assert multiplicator(*list_creator) == multiple_sum
