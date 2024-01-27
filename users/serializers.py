from rest_framework import serializers
from users.models import SimpleUser


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUser
        fields = "__all__"
