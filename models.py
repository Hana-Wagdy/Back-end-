from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser
    """
    class Role(models.TextChoices):
        USER = 'user', _('Regular User')
        ADMIN = 'admin', _('Administrator')
    
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
        verbose_name=_('User Role')
    )
    
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        verbose_name=_('Profile Picture')
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser