"""
ЗАДАЧА
Написать реализацию функции closest_mod_5

ВХОДНЫЕ ДАННЫЕ:
    целое число x
ВЫХОДНЫЕ ДАННЫЕ:
    самое маленгькое целое число y, такое что:
            - y больше или равно x
            - y делится нацело на 5

"""


def closest_mod_5(x):
    y = x
    if y >= x and y % 5 == 0:
        return y
    else:
        return closest_mod_5(y+1)


print(closest_mod_5(11))
