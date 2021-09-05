# https://www.youtube.com/watch?v=EBMXOsCL9AA
# self.assertEqual() - очікуємо на результат
# self.assertRaises() - очікуємо на помилку
# self.assertIsInstance(,) - очікуємо відповідність до якогось типу (int, str, list, tuple, ..)

from unittest import TestCase
from solver import add, square_equation_solver, TYPE_ERROR_TEXT
import pytest  # - імпортємо для №8 (перероблюємо тести під pytest)
#1
class TestAddCase(TestCase):  # ствроюємо клас TestAddCase (що наслідується від класу TestCase) — тестування Unittest(по замовчуванню)
    def test_ok(self):
        res = add(1, 2)
        self.assertEqual(res, 3, 'Тест не пройдено!')



#2 той самий тест але вже через pytest (може працювати і без self)
def test_add():
    res = add(1, 2)
    assert res == 3




#3 тестуємо квадратне рівняння
class TestSquareEquationSolver1(TestCase):  # щоб вилізла помилка, якщо буде передано неправильний тип даних
    def test_raises_type_error1(self):
        try:
            square_equation_solver('', 1, 1.5)
        except TypeError as e:
            print('OK, errored', e)  # >> OK, errored Not valid type for param
        else:
            self.fail('Did not raise')

#4 через те, що не зручно постійно писати  try, except, else і можна щось забути, є більш коротка форма тесту:
class TestSquareEquationSolver2(TestCase):  # щоб вилізла помилка, якщо буде передано неправильний тип даних
    def test_raises_type_error2(self):
        with self.assertRaises(TypeError):
            square_equation_solver('', 1, 1.5)  # якщо написати (2, 1, 1.5) то буде >> AssertionError: TypeError not raised
#5
    def test_result_is_tuple(self):  # тест на те, що a, b це пара (tuple)
        res = square_equation_solver(0, 0, 0)  # a, b, c - не важливо які значення, бо перевірка тільки на пару
        self.assertIsInstance(res, tuple)  # assertIsInstance - ассерт відповідності типу tuple
#6
    def test_no_results(self):  # тест, щоб при a = 0, b = 0 >> return None, None
        res = square_equation_solver(0, 0, 1)  # c = 1 - будь-яке число
        self.assertEqual(res, (None, None))
#7
    def test_solves_ok(self):  # тест перевірка правильності обчислення коренів квадр. рівняння
        res = square_equation_solver(1, -3, -4)  # - при таких значеннях
        self.assertEqual(res, (4, -1))  # - повинен бути такий результат


#8 перероблюємо наші тести під pytest:
class TestSquareEquationSolver:
    def test_raises_type_error(self):
        with pytest.raises(TypeError) as exc_info:
            square_equation_solver('', 1, 1.5)
        assert str(exc_info.value) == TYPE_ERROR_TEXT

    def test_result_is_tuple(self):  # тест на те, що a, b це пара (tuple)
        res = square_equation_solver(0, 0, 0)
        assert isinstance(res, tuple)
    #9
    # @pytest.mark.parametrize('args, expected_result', [  # @pytest.mark.parametrize - @декоратор
    #     ((1, -3, -4), (4, -1)),  # (при таких значеннях), (очікуємо на такий результат)
    #     ((0, 0, 0), (None, None)),
    # ])

    #10
    @pytest.mark.parametrize('args, expected_result', [  # @pytest.mark.parametrize - @декоратор
        pytest.param(
            (1, -3, -4), (4, -1),
            id='general', # - називаємо тест, щоб було видно в результатах (Test Results)
        ),
        pytest.param(
            (0, 0, 0), (None, None),
            id='no results',
        ),
    ])
    def test_solves_ok(self, args, expected_result):
        res = square_equation_solver(*args) # args - передаємо у функцію всі аргументи(1, -3, -4) і розпаковуємо tuple за допомогою *
        assert res == expected_result
