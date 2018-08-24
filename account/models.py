from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email,date_of_birth,password=None):
        if not email:
            raise ValueError("Enter the email")
        if password is None:
            raise ValueError("Enter the Password")
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,date_of_birth, password=None):
        user = self.create_user(email, date_of_birth, password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)

    def create_staffuser(self, email, date_of_birth, password=None):
        user = self.create_user(email,date_of_birth,  password)
        user.staff = True
        user.save(using=self._db)


class User(AbstractBaseUser):

    email = models.EmailField(max_length=255, unique=True)
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=7, choices=gender_choice)
    date_of_birth = models.DateField()
    avatar = models.ImageField()
    last_login = models.DateTimeField(auto_now=True)
    email_verified = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    objects = UserManager()
