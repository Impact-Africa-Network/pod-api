from .managers import IANUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from dataclasses import dataclass
from ian_account.utils import user_avatar_directory


@dataclass
class IANStatus:
    """
    IAN User Statuses
    """
    NEW: str = "NEW"
    ACTIVE: str = "ACTIVE"
    SUSPENDED: str = "SUSPENDED"
    DELETED: str = "DELETED"
    PENDING_KYC_UPLOAD: str = "PENDING_KYC_UPLOAD"
    PENDING_KYC_APPROVAL: str = "PENDING_KYC_APPROVAL"
    KYC_DOCS_REJECTED: str = "KYC_DOCS_REJECTED"
    KYC_DOCS_ACCEPTED:str = "KYC_DOCS_ACCEPTED"

@dataclass
class Gender:
    MALE: str = "M"
    FEMALE: str = "F"


@dataclass
class DocumentCheckList:
    NATIONAL_ID: str = "NATIONAL-ID"
    PASSPORT: str = "PASSPORT"
    BIRTH_CERTIFICATE: str = "BIRTH-CERTIFICATE"
    DRIVING_LICENCE: str = "DRIVING-LICENCE"
    HUDUMA_NUMBER: str = "HUDUMA-NUMBER"
    KYC_SELFIE: str = "KYC-SELFIE"

class IANUser(AbstractBaseUser, PermissionsMixin):
    """
    IANUser Base Model
    """
    id = models.BigAutoField(primary_key=True, unique=True)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=40, default=IANStatus.NEW)
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = IANUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []



class User(IANUser):
    """
    IAN User Model
    """
    first_name = models.CharField("first name", max_length=30, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    login_attempts = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, blank=True, null=True)
    token = models.TextField(default="")
    avatar = models.ImageField(blank=True, null=True, upload_to=user_avatar_directory, default="default_avatar.jpeg")

    @property
    def too_many_login_attempts(self) -> bool:
        """
        Check if user has exceeded login attempts threshold.
        """
        return self.login_attempts > 2

    def sms_user(self, msg) -> bool:
        """
        SMS User.

        TODO:

            - Should trigger a celery task
            - Celery task should in turn call the notification service with appropriate params
        """
        return True

    def email_user(self, subject, body, **kwargs) -> bool:
        """
        Email User.

        TODO:

            - Should trigger a celery task
            - Celery task should in turn call the notification service with appropriate params
        """
        return True

    def get_full_name(self) -> str:
        """
        Return the first_name and the last_name.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip().title()

    def get_display_name(self) -> str:
        """Returns Display Name"""
        return f"{self.first_name.title()} {self.last_name.title()}"

    def get_short_name(self) -> str:
        """Return the short name for the user."""
        return self.first_name.title()

    def generate_token(self):
        """
        Generate User Token
        """
        from ian_auth import encryption, exceptions

        from . import serializers as sz

        ian_encryption = encryption.ian_encryption
        serialzer = sz.UserTokenSerializer(self)
        data = serialzer.data
        ttl = 60 * 24 * 30 * 12  # TTL = 1 Year
        message = ian_encryption.make_token(data, time_to_live=ttl)
        if not message[0]:
            raise exceptions.IANEncryptionError(value=message[1])
        return message[1]











