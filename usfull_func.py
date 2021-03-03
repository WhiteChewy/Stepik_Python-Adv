# поиск пути по графу на вход подается сам словарь графа конец пути, начало
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