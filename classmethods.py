"""@classmethod – это обычный метод класса, имеющий доступ ко всем атрибутам класса, через который он был вызван.
Следовательно, classmethod – это метод, который привязан к классу, а не к экземпляру класса."""


class MyClass:
    @classmethod
    def foo(cls):
        print("class method called")


MyClass.foo()
# class method called

MyClass().foo()
# class method called

my_object = MyClass()
my_object.foo()
# class method called

"""classmethod может изменять состояние класса, но не может изменять состояние конкретного экземпляра класса."""


class MyClass:
    VALUE = 0

    @classmethod
    def foo(cls):
        print(cls.VALUE)


MyClass.foo()
# 0

MyClass().foo()
# 0

my_object = MyClass()
my_object.foo()
# 0


class MyClass:
    VALUE = 0

    def __init__(self):
        self.value = 0

    @classmethod
    def foo(cls):
        print(cls.value)


# my_object = MyClass()
# my_object.foo()
# AttributeError: type object 'MyClass' has no attribute 'value'


"""Если метод класса, декорируемый @classmethod вызывается для производного класса,
 то объект производного класса передается как подразумеваемый первый аргумент."""


class MyClass:
    VALUE = 0

    @classmethod
    def foo(cls):
        print(cls.VALUE)


class MyChild(MyClass):
    VALUE = 1

    @classmethod
    def child_foo(cls):
        print(cls.VALUE)


MyChild.child_foo()
# 1


class MyClass:
    @classmethod
    def method(cls, arg):
        print(f"{cls.__name__}.method  {arg}")

    @classmethod
    def call_orig_metod(cls):
        cls.method(1)

    def call_metod(self):
        self.method(2)


class MyChild(MyClass):
    @classmethod
    def call_orig_metod(cls):
        cls.method(3)


MyClass.method(0)
# MyClass.method  0

MyClass.call_orig_metod()
# MyClass.method  1

MyChild.method(0)
# MyChild.method  0

MyChild.call_orig_metod()
# MyChild.method  3

a_obj = MyClass()
a_obj.method(1)
# MyClass.method  1

a_obj.call_orig_metod()
# MyClass.method  1

a_obj.call_metod()
# MyClass.method  2
