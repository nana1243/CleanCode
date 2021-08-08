import re

EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+\.[^@]+")

def is_valid_email(candidates:str):
    return re.match(EMAIL_FORMAT,candidates)


class User:
    def __init__(self,username:str):
        self.username = username
        self._email = None

    @property
    def email(self,new_email):
        if not is_valid_email(new_email):
            raise ValueError(f" Cant set {new_email}")
        self._email = new_email