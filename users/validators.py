import re
from django.core.exceptions import ValidationError

def validate_password(filed):
    pattern = re.compile(r'^[A-Za-z0-9]+$')
    if not bool(re.match(pattern,filed)):
        ex = 'Пароль должен только содержать латинские буквы и цифры'
        print(ex)
        raise ValidationError (ex)
    if not 8<= len(filed) <=16:
        ex = "Пароль должен быть от 8 до 16 символов"
        print(ex)
        raise ValidationError(ex)

