from django.urls import path, include
from rest_framework import routers
from api.apiviews.topic_apiviews import TopicViewSet
#from api.apiviews.student_apiviews import student_list, student_detail
from api.apiviews.message_apiviews import MessageViewSet
from api.apiviews.forums_apiviews import ForumViewSet

routers = routers.DefaultRouter()
routers.register(r'forums', ForumViewSet, basename='forums')
routers.register(r'topics', ForumViewSet, basename='topics')
routers.register(r'messages', ForumViewSet, basename='messages')


app_name = 'api'
urlpatterns = [
    path('', include(routers.urls)),
]