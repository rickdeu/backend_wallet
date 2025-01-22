from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(_('phone number'), max_length=150, blank=True, null=True, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    company_name = models.CharField(_('company name'), max_length=250, blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=130, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    ip_address = models.GenericIPAddressField(_('ip address'), blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email



    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['email']


