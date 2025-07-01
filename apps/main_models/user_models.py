from django.db import models 
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
import uuid
from django.utils import timezone
from django.core.exceptions import ValidationError 


def validate_profile_image_size(image):
    max_size = 15 * 1024 * 1024 
    if image.size > max_size:
        raise ValidationError("The image size cannot exceed 10 MB.")
    
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, is_active=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(username, password=password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=255, unique=True)
    first_name= models.CharField(max_length=255, null=True, blank=True, verbose_name="First name")
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Last name")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="Phone number")
    national_code = models.CharField(max_length=10, unique=True, verbose_name="National code")
    
    GENDER_TYPE_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("choose_not_to_say", "I prefer not to say")
    ]
    gender = models.CharField(max_length=255, choices=GENDER_TYPE_CHOICES, verbose_name="Gender")

    birth_date = models.DateField(blank=True, null=True) 

    USER_TYPE_CHOICES = [
        ("doctor", "Doctor"),
        ("patient", "Patient")
    ]
    user_type = models.CharField(max_length=255, choices=USER_TYPE_CHOICES, verbose_name="User type", default="patient")
    profile_image = models.ImageField(upload_to="profiles/", null=True, blank=True, verbose_name="Profile Image", validators=[validate_profile_image_size])

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    join_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'national_code', 'user_type']
    
    def __str__(self):
        return f"{self.username} ({self.user_type})"
    
    class Meta:
        ordering = ["-join_date"]