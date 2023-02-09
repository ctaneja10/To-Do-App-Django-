from django.db import models

# Create your models here.
class tasks(models.Model):
    task_slug = models.IntegerField(default=0)
    title_main = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=500)

    def __str__(self):
        return self.title_main

