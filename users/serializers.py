from rest_framework import serializers
from users.models import SimpleUser

from users.producer import ProducerUserCreated
from django.http import JsonResponse

producer_user_created = ProducerUserCreated()


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUser
        fields = "__all__"

    def create(self, validated_data):
        producer_user_created.publish(
            "user_created_method",
            validated_data,
        )

        user = SimpleUser.objects.create(**validated_data)

        return JsonResponse(
            {
                "message": "User signed up successfully",
                "user": {
                    "id": user.id,
                    "username": user.name,
                    "email": user.email,
                },
            }
        )
