"""
ЗАДАЧА

реализовать структуру данных стек, которая представляет собой "расширение" структуры list

необходимо поддержать добавление элемента на вершину стека, удаление с вершины стека,
и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления.

Описание операций

Сложение: снимается верхний элемент и к нему прибавляется верхний элемент, результат
          кладется на вершину стека
остальные операции действуют по тому же принципу

Создаваемый класс должен иметь вид:
class ExtendedStack(list):
    def sum(self):
        # операция сложения

    def sub(self):
        # операция вычитания

    def mul(self):
        # операция умножения

    def div(self):
        # операция целочисленного деления
"""


class ExtendedStack(list):
    def sum(self):
        self.append(self.pop()+self.pop())

    def sub(self):
        self.append(self.pop()-self.pop())

    def mul(self):
        self.append(self.pop()*self.pop())

    def div(self):
        self.append(self.pop()//self.pop())


# проверка
x = ExtendedStack()
x.extend([1, 2, 3, 4, 5, 6])
print(x)
x.sum()
print(x)
x.sub()
print(x)
x.mul()
print(x)
x.div()
print(x)
