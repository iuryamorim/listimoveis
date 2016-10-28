from django.core.exceptions import ValidationError


def validate_cep(value):
    tam = len(str(value))
    if tam != 8:
        raise ValidationError('Cep inválido')
    for i in value:
        try:
            x = int(i)
        except:
            raise ValidationError('Somente números')