from rest_framework import serializers
from .models import Teammate


class TeammateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teammate
        fields = '__all__'