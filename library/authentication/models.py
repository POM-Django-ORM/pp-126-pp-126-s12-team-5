from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone

ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
)

class CustomUser(AbstractBaseUser):
    """
    This class represents a basic user.

    Attributes:
    -----------
    first_name: str, max length=20
    last_name: str, max length=20
    middle_name: str, max length=20
    email: str, unique, max length=100
    password: str
    created_at: int (timestamp)
    updated_at: int (timestamp)
    role: user role, default role (0, 'visitor')
    is_active: bool, default=False
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name} ({self.email})'

    def __repr__(self):
        return f"<CustomUser id={self.id} email={self.email}>"

    @staticmethod
    def get_by_id(user_id):
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None

    @staticmethod
    def get_by_email(email):
        try:
            return CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            user.delete()
            return True
        except CustomUser.DoesNotExist:
            return False

    @staticmethod
    def create(email, password, first_name=None, middle_name=None, last_name=None):
        user = CustomUser(
            email=email,
            password=password,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
        )
        user.set_password(password)  # Set password using Django's hashing
        user.save()
        return user

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'email': self.email,
            'created_at': int(self.created_at.timestamp()),
            'updated_at': int(self.updated_at.timestamp()),
            'role': self.role,
            'is_active': self.is_active,
        }

    def update(self, first_name=None, last_name=None, middle_name=None, password=None, role=None, is_active=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if middle_name:
            self.middle_name = middle_name
        if password:
            self.set_password(password)
        if role is not None:
            self.role = role
        if is_active is not None:
            self.is_active = is_active
        self.save()

    @staticmethod
    def get_all():
        return CustomUser.objects.all()

    def get_role_name(self):
        return dict(ROLE_CHOICES).get(self.role, 'visitor')
