import logging


class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        logging.info(
            "Call: %s.__get__(%r, %r)",
            self.__class__.__name__,
            instance,
            owner,  # noqa : E501
        )
        return instance


class ClientClass:
    descriptor = DescriptorClass()


if __name__ == "__main__":
    c = ClientClass()
    print(c.descriptor is c)
