from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from api.serializer.message_serializer import MessageSerializer
from blog.models.message_models import MessageModel


class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer