import re
from .field_class import Field
from src.utils import InvalidPhoneNumberError


class Phone(Field):
    def __init__(self, value) -> None:
        if not self.validate(value):
            raise InvalidPhoneNumberError(value)
        super().__init__(value)

    @staticmethod
    def validate(phone_number) -> bool:
        return re.fullmatch(r'\d{10}', phone_number) is not None