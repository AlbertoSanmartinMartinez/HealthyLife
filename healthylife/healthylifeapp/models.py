from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_chef = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    is_shop = models.BooleanField(default=False)

    class Meta:
        db_table = "auth_user"


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# https://es.stackoverflow.com/questions/930/roles-de-usuarios-en-django
