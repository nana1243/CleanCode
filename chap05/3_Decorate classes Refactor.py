import datetime
from dataclasses import dataclass
from typing import Callable, Dict


def hide_field(field: str) -> str:
    print(field)
    return "**redacted**"


def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")


def show_original(event_field):
    return event_field


class EventSerializer:
    def __init__(self, serialization_fields: Dict[str, Callable]):
        self.serialization_fields = serialization_fields

    def serialize(self, event) -> Dict:
        return {
            field: transformation(getattr(event, field))
            for field, transformation in self.serialization_fields.items()
        }


class Serialization:
    def __init__(self, **transformations):
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        return event_class


@Serialization(
    username=show_original,
    password=hide_field,
    ip=show_original,
    timestamp=format_time,  # noqa :E501
)
@dataclass
class LoginEvent:
    def __init__(self, username: str, password: str, ip: str, timestamp: str):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp
