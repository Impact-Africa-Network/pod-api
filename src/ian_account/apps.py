from django.apps import AppConfig

# from django.utils.translation import ugettext_lazy as _


class IanAccountConfig(AppConfig):
    name = 'ian_account'
    verbose_name = "Accounts"

    def ready(self) -> None:
        """
        Register IAN account signals
        """
        import ian_account.signals
