import re

from django.core.exceptions import ValidationError

class Validation:
    def email_validate(value):
        REGEX_EMAIL= '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(REGEX_EMAIL, value):
            raise ValidationError('INVALID_EMAIL')

    def password_validate(value):
        REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[?!@#$%*&])[A-Za-z\d?!@#$%*&]{8,}$'
        if not re.match(REGEX_PASSWORD, value):
            raise ValidationError('INVALID_PASSWORD')