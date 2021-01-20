from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, user_type, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('Email must be needed.')
        
        if not user_type:
            raise ValueError('User type must be needed.')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email, user_type, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self,email, user_type, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email,user_type, password, **extra_fields)






class User(AbstractBaseUser):
    choices = (
        ('A', 'Admin'),
        ('U', 'User'),
        ('I', 'Instructor')
    )
    Full_name = models.CharField(max_length = 150, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length = 150, blank=True, null=True)
    location = models.CharField(max_length = 50, blank=True, null=True)
    user_type = models.CharField(max_length=1, choices=choices)
    profile_pic = models.ImageField(blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']


    objects = UserManager()



