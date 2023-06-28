from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number=phone_number, password=password, **extra_fields)

    def create_user(self, phone_number=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The phone number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class Teacher(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150)
    grade = models.OneToOneField('students.Grade', related_name='grade', on_delete=models.CASCADE, blank=True, null=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='teacher_set',
        related_query_name='teacher'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='teacher_set',
        related_query_name='teacher'
    )

    def save(self, *args, **kwargs):
        self.username = self.phone_number  # Используем phone_number вместо username
        super().save(*args, **kwargs)
