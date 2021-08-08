import contextlib


def stop_database():
    print("stop database")

def start_database():
    print("start database")

def db_backup():
    print("db back_up!")

@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()


with db_handler():
    db_backup()




class dbhandler_decorator(contextlib.ContextDecorator):
    ...

