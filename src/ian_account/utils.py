import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone


def user_avatar_directory(instance, filename) -> str:
    """
    Avatar Upload Dir.
    """
    extension = filename.split(".")[-1]
    fname = f"{(int(timezone.now().timestamp()))}.{extension}"
    return f"accounts/files/{instance.email}/{fname}"



class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk)
            + six.text_type(timestamp)
            + six.text_type(user.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()
