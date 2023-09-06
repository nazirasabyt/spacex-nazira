from rest_framework.serializers import ModelSerializer
from .models import Link
from .models import Advantage

class LinkSerializer(ModelSerializer):
    class Meta:
        model=Link
        fields="__all__"

class AdvSerializer(ModelSerializer):
    class Meta:
        model=Advantage
        fields="__all__"