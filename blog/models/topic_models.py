from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from blog.models.forums_models import ForumModel



class TopicModel(DateTimeModel):
    forum = models.ForeignKey(ForumModel, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    libelle = models.CharField(max_length=20)
    

    def __str__(self):
        return f'{self.title}'
   