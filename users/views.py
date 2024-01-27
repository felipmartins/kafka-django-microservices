from rest_framework import viewsets
from users.models import SimpleUser
from users.serializers import SimpleUserSerializer


class SimpleUserViewSet(viewsets.ModelViewSet):
    queryset = SimpleUser.objects.all()
    serializer_class = SimpleUserSerializer
