from enum import IntEnum


# Type of product
class TYPES(IntEnum):
    FLAT = 0
    ROOM = 1

    @classmethod
    def select_types(cls):
        return [(key.value, key.name) for key in cls]


class ROLE(IntEnum):
    CUSTOMER = 0
    MANAGER = 1
    ACCOUNT = 2
    ADMIN = 3

    @classmethod
    def select_role(cls):
        return [(key.value, key.name) for key in cls]