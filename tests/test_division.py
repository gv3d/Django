from utils import division
import pytest

#1
def test_division_good1():
    assert division(10, 2) == 5
    assert division(10, 5) == 2
    assert division(20, 2) == 10
    assert division(10, -2) == -5

# 2
def test_division_one_more():
    assert division(10, 5) == 2

# 3 створюємо декоратор, щоб зменшити повторюваність коду в тестах:
@pytest.mark.parametrize('a, b, expected_result', [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])  # - два аргументи і результат
def test_division_good2(a, b, expected_result):
    assert division(a, b) == expected_result

# 4
def test_zero_division():
    with pytest.raises(ZeroDivisionError):  # тест на виключення (ділення на нуль)
        division(10, 0)

def test_type_error():
    with pytest.raises(TypeError):  # еусе на виключення (str замість int)
        division(10, '2')

# 5 об'єднаємо два тести з #4:

@pytest.mark.parametrize('div, divider, exp_error', [(10, 0, ZeroDivisionError),
                                                     (10, '2', TypeError)])

def test_zero_with_type_error(div, divider, exp_error):
    with pytest.raises(exp_error):
        division(div, divider)
