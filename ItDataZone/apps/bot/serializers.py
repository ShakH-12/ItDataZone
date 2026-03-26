from rest_framework import serializers
from .models import User, RegisteredUser


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


class RegisterToCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = ["user", "phone", "course", "course_price"]
        read_only_fields = ("course_price",)

    def create(self, validated_data):
        validated_data["course_price"] = validated_data["course"].price
        return RegisteredUser.objects.create(**validated_data)