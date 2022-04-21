from django.http  import JsonResponse, HttpResponse
import re
from users.models import User
from django.core.exceptions import ValidationError

class Validation:
    def email_validate(value):
        REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(REGEX_EMAIL, 'email'):
            raise ValidationError('INVALID_EMAIL')
    def password_validate(value):
        REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[?!@#$%*&])[A-Za-z\d?!@#$%*&]{8,}$'
        if not re.match(REGEX_PASSWORD, 'password'):
            raise ValidationError('INVALID_PASSWORD')