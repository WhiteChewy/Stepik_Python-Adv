"""
ЗАДАЧА

Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом,
чтобы при добавлении элемента в список посредством метода append в лог отправлялось
сообщение, состоящее из только что добавленного элемента.

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
"""
import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, x):
        elem = super(LoggableList, self).append(x)
        return self.log(x)


x = LoggableList()
x.append(1)
x.append(0)
x.append(12)
print(x)
