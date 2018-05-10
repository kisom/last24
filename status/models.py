from django.contrib.auth import models as auth_models
from django.db import models


class Project(models.Model):
    """
    A status item applies to a Project --- this is what I'm working on.
    """
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=2048)
    link = models.URLField()


class Tag(models.Model):
    """A tag allows work to be organised by the kind of work, too."""
    name = models.CharField(max_length=32)


class Status(models.Model):
    """What did you do?"""
    title = models.CharField(max_length=256)
    owner = models.ForeignKey(auth_models.User)
    restricted = models.ForeignKey(auth_models.Group, null=True, blank=True)
    notes = models.TextField(max_length=1024, null=True, blank=True)
    completed = models.BooleanField()
