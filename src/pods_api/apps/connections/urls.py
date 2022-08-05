from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('connections/',connections_list),
    path('connection-detail/<int:pk>',connection_detail),
]

urlpatterns=format_suffix_patterns(urlpatterns)