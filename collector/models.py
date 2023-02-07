from django.db import models
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone_number(value):
    if not re.match(r'^\+?\d+$', value):
        raise ValidationError(
            _('%(value)s is not a valid phone number'),
            params={'value': value},
        )

class Contact(models.Model):
    phone_number = models.CharField(validators=[validate_phone_number], max_length=20, unique=True)
    email = models.EmailField()
