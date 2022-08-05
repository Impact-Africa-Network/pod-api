from django.db import router
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

# router=DefaultRouter()
# router.register(r'connections',connections_list,basename='connections')
# router.register(r'connections-detail',connection_detail,basename='connection-detail')

# urlpatterns=router.urls+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns=[
    path('connections/',connections_list),
    path('connection-detail/<int:pk>',connection_detail),
]

urlpatterns=format_suffix_patterns(urlpatterns)