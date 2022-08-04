from django.contrib import admin
from ian_account.models import User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class UserModelAdmin(BaseUserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        """
        Customize the read only/disabled fields on the form
        """
        form = super().get_form(request, obj, **kwargs)
        # is_superuser = request.user.is_superuser
        # if not is_superuser:
        #     form.base_fields['email'].disabled = True
        # form.base_fields["token"].disabled = True
        # form.base_fields["created_time"].disabled = True
        return form

    search_fields = [
        "email",
        "first_name",
        "last_name",
    ]
    list_display = (
        "email",
        "first_name",
        "last_name",
    )
    # readonly_fields = ['token']
    ordering = [
        "email",
        "first_name",
        "created_time",
    ]
    fieldsets = (
        (
            _("Account"),
            {
                "fields": (
                    "email",
                    "status",
                    "password",
                )
            },
        ),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "gender","avatar")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("created_time",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "gender",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

