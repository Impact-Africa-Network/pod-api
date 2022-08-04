from django.db import connection
from django.urls import path
from connections import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('connections/',views.connections_list, name='connections'),
    path('connections-detail/<int:pk>',views.connection_detail, name='connections-details'),
]

urlpatterns=format_suffix_patterns(urlpatterns)