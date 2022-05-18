from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    uploaded_date = models.DateTimeField(auto_now_add=True, verbose_name='Загружена')
