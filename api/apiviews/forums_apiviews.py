from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from api.serializer.forums_serializer import ForumSerializer
from blog.models.forums_models import ForumModel


class ForumViewSet(viewsets.ModelViewSet):
    queryset = ForumModel.objects.all()
    serializer_class = ForumSerializer
    