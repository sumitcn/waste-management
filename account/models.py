from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
<<<<<<< HEAD
    def create_user(self,email,username,password=None):
=======
    def create_user(self,username ,email,password=None):
>>>>>>> development
        if not email:
            raise ValueError("Enter the email")
        # if password is None:
        #     raise ValueError("Enter the Password")
        user = self.model(

            email=self.normalize_email(email),
<<<<<<< HEAD
            username=username

=======
            username=username,
>>>>>>> development
            

        )
        user.set_password(password or None )
        user.save(using=self._db)
        return user

    def create_superuser(self, username ,email,  password=None):
        user = self.create_user(username ,email, password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)

    def create_staffuser(self,username , email,  password=None):
        user = self.create_user(username ,email,  password)
        user.staff = True
        user.save(using=self._db)


class User(AbstractBaseUser):

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255,unique=True)
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=7, choices=gender_choice)
    date_of_birth = models.DateField(default='1990-09-09')
    avatar = models.ImageField()
    last_login = models.DateTimeField(auto_now=True)
    email_verified = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

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
