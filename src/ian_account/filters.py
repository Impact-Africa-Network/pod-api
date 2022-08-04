from django_filters import rest_framework as filters

from ian_account.models import User


class UserFilter(filters.FilterSet):
    max_date = filters.DateTimeFilter(field_name="created", lookup_expr="lte")
    min_date = filters.DateTimeFilter(field_name="created", lookup_expr="gte")

    class Meta:
        model = User
        fields = (
            "max_date",
            "min_date",
            "is_superuser",
            "is_staff",
            "status",
            "is_active",
        )
