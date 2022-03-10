from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200)
    national_id = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    sub_county = models.CharField(max_length=20)
    village = models.CharField(max_length=20)

    class Meta:
        ordering = ["-pk"]



