from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUser(AbstractUser):
    num_doc_identificacion = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15)

    class Meta:
      swappable = 'AUTH_USER_MODEL'

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )