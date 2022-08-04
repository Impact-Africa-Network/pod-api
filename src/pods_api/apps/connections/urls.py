from django.urls import path
from connections import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('connections/',views.connections_list, name='connections'),
    path('connection-detail/<int:pk>',views.connection_detail, name='connection-details'),
]

urlpatterns=format_suffix_patterns(urlpatterns)