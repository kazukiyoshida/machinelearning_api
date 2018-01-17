from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)

class Photo(models.Model):
    user = models.ForeignKey(User, related_name="photo")
    title = models.CharField(max_length=64)


