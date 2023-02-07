import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('phone_number', 'email')

    def validate_email(self, value):
    # Regular expression for email format validation
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, value):
            raise ValidationError("Invalid email format")
        return value
