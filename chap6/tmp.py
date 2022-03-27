class MyProperty1:
    def __get__(self, instance, owner=None):
        return instance._y

    def __set__(self, instance, value):
        instance._y = value

    def __delete__(self, instance):
        del instance._y


class Point1:
    y = MyProperty1()

    def __init__(self):
        self.x = 0
        self.y = 0  # self.y.__set__(self.y, self, 0)


point = Point1()
print(point.__dict__)


class MyProperty:
    def __set_name__(self, owner, name):
        print(f"__set_name__(owner:{owner}, name:{name})")

    def __get__(self, instance, owner=None):
        print("running __get__")
        return instance._y

    def __set__(self, instance, value):
        print("running __set__")
        instance._y = value

    def __delete__(self, instance):
        del instance._y


class Point2:
    x = MyProperty()  # x.__set_name__(x, Point, 'x')
    y = MyProperty()  # y.__set_name__(y, Point, 'y')

    def __init__(self):
        self.x = 1  # self.x.__set__(self.x, self, 1)
        self.y = 2  # self.y.__set__(self.y, self, 2)


p = Point2()

# OUTPUT :
# __set_name__(owner:<class '__main__.Point'>, name:x)
# __set_name__(owner:<class '__main__.Point'>, name:y)
