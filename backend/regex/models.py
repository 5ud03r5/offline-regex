from django.db import models
import uuid
# Create your models here.

class Regex(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True, unique=True)
    text = models.TextField(max_length=1000, null=True, blank=True)
    regex = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')
    id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Tag(models.Model): 
    name = models.CharField(max_length=500, null=True, blank=True, unique=True)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True, editable=False)
    def __str__(self):
        return self.name