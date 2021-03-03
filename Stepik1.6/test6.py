"""
ЗАДАЧА

Дано описание наследование классов в следующем виде:

<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>

откуда следует что класс 1 унаследовано от класса 2, класса 3 и т.д.

или эквивалентно записи:

class Class1(Class2, Class3...ClassK):
    pass

Класс А является прямым предком класса B, если B отнаследован от A:
class B(A):
    pass

Класс A является предком класса B, если
- A = B;
- A - прямой предок B
- существует такой класс C, что C - прямой предок B и A - предок C

class B(A):
    pass

class C(B):
    pass

# A -- предок С

необходимо отвечать на запросы, является ли один класс предком другого класса

ВХОДНЫЕ ДАННЫЕ:
число классов.
определения классов
число запросов
запросы
"""
size = int(input())
d = dict()

# заполняем словарь наследования где ключ имя класса, значения список классов родителей
for i in range(size):
    cl = input().split()
    cl = cl[:1]+cl[2:]  # из строчки удаляется двоеточие
    for l in range(len(cl)):  # если в строке есть неизвестные классы такой класс "добавляется"
        if cl[l] not in d.keys():
            d[cl[l]] = []
    d[cl[0]] = cl[1:]  # добавить родителей классу

# print()
# print(d)
size = int(input())


def isAncestor(graph, end, start, path=[]):
    path = path + [start]
    # print(path)
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = isAncestor(graph, end, node, path)
            if newpath:
                return newpath
    return None


visited = []
level = []
# считываем запросы
for i in range(size):
    requests = input().split()
    if isAncestor(d, requests[0], requests[1]):
        print("Yes")
    else:
        print("No")
