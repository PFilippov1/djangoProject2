from django.db import models


class Schedule(models.Model):
    schedule_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


class Option(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)


from django.contrib.auth.models import User
# тип "временнАя зона" для получения текущего времени
from django.utils import timezone


class Message(models.Model):
    chat = models.ForeignKey(
        Schedule,
        verbose_name='Чат под загадкой',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField(
        'Дата сообщения',
        default=timezone.now)


class Mark(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        verbose_name='Расписание',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    mark = models.IntegerField(
        verbose_name='Оценка')
    pub_date = models.DateTimeField(
        'Дата оценки',
        default=timezone.now)
