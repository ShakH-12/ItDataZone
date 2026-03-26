from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "phone")
        read_only_fields = ("id",)

    def validate(self, attrs):
        if User.objects.filter(id=attrs["id"]).exists():
            raise serializers.ValidationError({"id": "User already exists"})
        return attrs


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "phone")
        read_only_fields = ("id",)


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"