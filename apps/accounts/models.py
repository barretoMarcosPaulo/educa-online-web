from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class User(AbstractBaseUser):
    name = models.CharField('Nome', max_length=255, blank=False, null=False)
    username = models.CharField('Nome de usuário', max_length=100, unique=True, null=True, blank=True)
    email = models.CharField('Email', max_length=100, unique=True, null=False, blank=False)

    is_staff = models.BooleanField('staff status', default=False)
    is_superuser = models.BooleanField('superuser', default=False)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def get_short_name(self):
        return self.name.split(' ')[0]

    def __str__(self):
        return self.name
