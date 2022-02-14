from rest_framework import serializers
from .models import ChatCode

class ChatCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatCode
        fields = (
            'show_name',
            'id',
        )
