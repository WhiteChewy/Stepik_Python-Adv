"""
Входные данные:
1-ая строка - количество чисел
Строки далее числа по одному

Выходные данные:
Сумма всех чисел

"""

size = int(input())
n = [int(input()) for i in range(size)]
print(sum(n))