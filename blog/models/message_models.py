from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from blog.models.topic_models import TopicModel



class MessageModel(DateTimeModel):
    topic = models.ForeignKey(TopicModel, related_name='messages', on_delete=models.CASCADE)
    objet = models.TextField()
    libelle = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.libelle} - {self.topic}'