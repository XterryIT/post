
from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(unique=True, max_length=20)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    is_register = models.BooleanField(default=False)

    class Meta: 
        db_table = 'Users'


