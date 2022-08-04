from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("manage", views.UserViewSet, basename="manage")
router.register("auth", views.UserAuthViewSet, basename="auth")

app_name = "ian_account"
urlpatterns = []

urlpatterns += router.urls
