from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from api.serializer.topic_serializer import TopicSerializer
from blog.models.topic_models import TopicModel


class TopicViewSet(viewsets.ModelViewSet):
    queryset = TopicModel.objects.all()
    serializer_class = TopicSerializer