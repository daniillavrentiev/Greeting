from django.db import models


class Greeting(models.Model):

    name = models.CharField(max_length=255, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=255, verbose_name='Прізвище')
    email = models.EmailField(max_length=255, verbose_name='Email')
    date = models.DateTimeField(auto_now=True, verbose_name='Время приветствия')

    def __str__(self):
        return self.name
