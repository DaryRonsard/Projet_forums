from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class ForumModel(DateTimeModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)



    def __str__(self):
        return f'{self.title} - {self.description}'
   