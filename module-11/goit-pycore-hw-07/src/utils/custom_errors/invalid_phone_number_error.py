class InvalidPhoneNumberError(Exception):
    def __init__(self, phone_number):
        super().__init__(f"Invalid phone number {phone_number}. Must be exactly 10 digits.")