from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from apps.user.managers import UserManager

def user_avatar_bucket(instance, filename):
    return f'users/avatars/{filename}'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name=_('email address'))
    name = models.CharField(max_length=100, verbose_name=_('full name'))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('date joined'))
    is_staff = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
        verbose_name=_('staff status'),
    )
    is_active = models.BooleanField(default=True, verbose_name=_('active'))
    avatar = models.ImageField(upload_to=user_avatar_bucket, null=True, blank=True, verbose_name=_('avatar'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.name

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.name.split(' ')[0]

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
