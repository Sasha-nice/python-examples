"""
staticmethod - создает метод, который ничего не знает о классе или экземпляре
"""


class MyClass:
    @staticmethod
    def foo():
        print("static method called")

    def non_static_foo(self):
        print("non static method called")


MyClass.foo()
# static method called

MyClass().foo()
# static method called

my_object = MyClass()
my_object.foo()
# static method called


MyClass.non_static_foo()
# TypeError: MyClass.non_static_foo() missing 1 required positional argument: 'self'

MyClass().non_static_foo()
# non static method called

my_object = MyClass()
my_object.foo()
# non static method called


"""staticmethod не имеет доступа к классу или его экземплярам"""


class MyClass:
    def __init__(self):
        self.value = 10

    @staticmethod
    def foo(self):
        print(self.value)


my_object = MyClass()
my_object.foo()
# TypeError: MySecondClass.foo() missing 1 required positional argument: 'self'


"""Если убрать декоратор @staticmethod, то ошибки не будет"""


class MyClass:
    def __init__(self):
        self.value = 10

    def foo(self):
        print(self.value)


my_object = MyClass()
my_object.foo()
# 10

"""Статические методы делают код более читаемым и повторно используемым"""


class Validator:
    @staticmethod
    def validate_int(value):
        return isinstance(value, int)

    @staticmethod
    def validate_str(value):
        return isinstance(value, str)


"""В другом модуле достаточно будет сделать
import Validator

вместо

import validate_int, validate_str, ...
"""
