from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            'show_name',
            'id',
            'group_type',
            'show_name',
            'year',
            'sem_tri',
        )
