from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class CustomUserManager(BaseUserManager):
    def create_user(self,email, full_name=None,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("Password is required")
        
        
        user = self.model(
            email = self.normalize_email(email),
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self,email,full_name=None,password=None):
        user = self.create_user(
            email,
            password=password,
            
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,email,full_name=None,password=None):
        user = self.create_user(
            email,
            password=password,
            
        )
        user.active = True
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, blank=False)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, blank=False)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    


    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
    
