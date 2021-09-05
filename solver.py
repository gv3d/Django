# https://www.youtube.com/watch?v=EBMXOsCL9AA

from math import sqrt  # для №6 імпортуємо функцію квадр.кореня sqrt(square root)
TYPE_ERROR_TEXT = 'Not valid type for param'
# 1): пройшов тест
# def add(a, b):
#     return a + b

#2): не пройшов тест
# def add(a, b):
#     res = a + b
#     print(f'{a} + {b} = {res}')

#3): пройшов тест (дописали return res)
def add(a, b):
    res = a + b
    print(f' {a} + {b} = {res}')
    return res

# 4): перевіряємо аргумент "а" на int, float
# def square_equation_solver(a, b ,c):
#     if not isinstance(a, (int, float)):
#         raise TypeError('Not valid type for param')
#     pass

# 5): перевіряємо всі (all) аргументи "а, b, c" на int, float за допомогою лямбди
# def square_equation_solver(a, b ,c):
#     if not all(
#         map(lambda p: isinstance(p, (int, float)),
#             (a, b, c),)
#     ):
#         raise TypeError('Not valid type for param')
#     print('Types are OK')

# 6): дописуємо до №5 умови для квадратного рівняння, дискримінант:
def square_equation_solver(a, b ,c):
    if not all(
        map(lambda p: isinstance(p, (int, float)),
            (a, b, c),)
    ):
        raise TypeError(TYPE_ERROR_TEXT)
    if a == 0:
        if b == 0:
            return None, None
        return -c / b, None
    # дискримінант:
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None, None
    d_root = sqrt(d)
    x1 = (-b + d_root) / 2 * a
    x2 = (-b - d_root) / 2 * a
    if d == 0:
        x2 = None
    elif x2 > x1:
        x1, x2 = x2, x1
    return x1, x2

