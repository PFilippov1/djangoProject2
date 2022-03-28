from django.db import models


class Schedule(models.Model):
    schedule_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


class Option(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
