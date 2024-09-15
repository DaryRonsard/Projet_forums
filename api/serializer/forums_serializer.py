from rest_framework import serializers
from blog.models.forums_models import ForumModel


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumModel
        fields = '__all__'