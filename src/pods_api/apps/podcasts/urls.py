from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('podcasts/',podcasts_list),
    path('podcasts-detail/<int:pk>',podcast_detail),
]


urlpatterns=format_suffix_patterns(urlpatterns)