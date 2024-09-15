from rest_framework import serializers
from blog.models.topic_models import TopicModel


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = '__all__'