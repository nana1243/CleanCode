import datetime
from typing import Dict


class LoginEventSerializer:
    def __init__(self, event):
        self.event = event

    def serialize(self) -> Dict:
        return {
            "user_name": self.event.username,
            "password": "**redacted**",
            "ip": self.event.ip,
            "timestamp": self.event.timestamp.strftime("%Y-%m-%d%H:%M"),
        }


class LoginEvent:
    SERIALIZER = LoginEventSerializer

    def __init__(
        self,
        username: str,
        password: str,
        ip: str,
        timestamp: datetime.datetime,  # noqa: E501
    ):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def serialize(self):
        return self.SERIALIZER(self).serialize()


# after Refactoring
