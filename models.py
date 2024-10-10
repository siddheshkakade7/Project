from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()