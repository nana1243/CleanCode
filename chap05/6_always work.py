import logging
from functools import wraps
from types import MethodType

logger = logging.getLogger(__name__)


class DBDriver:
    def __init__(self, dbstring):
        self.dbstring = dbstring

    def execute(self, query):
        return f"query {query} at {self.dbstring}"


def inject_db_driver(function):
    @wraps(function)
    def wrapped(dbstring):
        return function(DBDriver(dbstring))

    return wrapped


@inject_db_driver
def run_query(driver):
    return driver.execute("test_function")


# 하지만 같은 데코레이터를 클래스 메서드에 적용하면 인자에 self가 있어 동작하지 않는다.
# 이를 해결하기 위해서는 디스크립터 프로토콜을 구현한 데코레이터 객체를 만들 수 있다.


class inject_db_driver:
    def __init__(self, function):
        self.function = function
        wraps(self.function)(self)

    def __call__(self, dbstring):
        return self.function(DBDriver(dbstring))

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.__class__(MethodType(self.function, instance))
