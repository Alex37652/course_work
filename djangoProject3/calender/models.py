from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    @property
    def get_html_url(self):
        url = reverse('calender:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class CustomUser(AbstractUser):
    group = models.CharField(max_length=255)


class Category(models.Model):
    category = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.category
