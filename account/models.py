from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from ckeditor.fields import RichTextField

class User(AbstractBaseUser):
    # the password and last login are already exist
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='users/images/', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    # shows the validation based on:
    USERNAME_FIELD = 'phone_number'
    # the password is already exist and the USERNAME FIELD is too , REQUIRED FIELDS are just for createsuperuser
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'
