from django.db import router
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

# router=DefaultRouter()
# router.register(r'podcasts',podcasts_list,basename='podcasts')
# router.register(r'podcasts-detail',podcast_detail,basename='podcast-detail')

# urlpatterns=router.urls+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns=[
    path('podcasts/',podcasts_list),
    path('podcasts-detail/<int:pk>',podcast_detail),
]


urlpatterns=format_suffix_patterns(urlpatterns)