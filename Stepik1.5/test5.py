"""
ЗАДАЧА

Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается
целым числом – количеством монет, которые можно положить в копилку.
Класс должен поддерживать информацию о
    количестве монет в копилке,
    предоставлять возможность добавлять монеты в копилку
    узнавать, можно ли добавить в копилку ещё какое-то количество монет,
        не превышая ее вместимость.

Гарантируется, что метод add(self, v)
будет вызываться только если can_add(self, v) – True.
"""


class MoneyBox:


    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        if self.money + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.money += v
            return self.money
        else:
            return -1
