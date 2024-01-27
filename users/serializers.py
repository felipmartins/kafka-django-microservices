from rest_framework import serializers
from users.models import SimpleUser

# from config import settings
from django.http import JsonResponse


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUser
        fields = "__all__"

    def create(self, validated_data):
        user_data = {}  # Retrieve user data from the request
        # producer.produce(
        #     settings.USER_EVENTS_TOPIC,
        #     key="user_signup",
        #     value=validated_data,
        # )
        # producer.flush()
        user = SimpleUser.objects.create(**user_data)

        return JsonResponse(
            {
                "message": "User signed up successfully",
                "user": user,
            }
        )
