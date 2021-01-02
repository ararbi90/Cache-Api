from django.db import models

# Create your models here.
class Log(models.Model):
    user_name = models.CharField(max_length=200)
    method = models.CharField(max_length=200, default='na')
    pub_date = models.DateTimeField('date published')
