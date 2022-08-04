from django.urls import path
from podcasts import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('podcasts/',views.podcasts_list  , name='podcasts'),
    path('podcasts-detail/<int:pk>',views.podcast_detail, name='podcast-details'),
]


urlpatterns=format_suffix_patterns(urlpatterns)