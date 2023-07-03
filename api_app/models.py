from django.db import models
from django.db import models
from phone_field import PhoneField

class  UserItem(models.Model):
    user_name = models.CharField(max_length=10)
    user_last_name = models.CharField(max_length=10)
    user_number = PhoneField(blank=True, help_text='Contact phone number')

