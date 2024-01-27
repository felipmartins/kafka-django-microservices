from django.urls import path, include
from rest_framework import routers
from users.views import SimpleUserViewSet


router = routers.DefaultRouter()

router.register(r"users", SimpleUserViewSet, basename="user")


urlpatterns = [
    path("", include(router.urls)),
]
