from rest_framework import serializers
from blog.models.message_models import MessageModel


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'