from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 225)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Interest(models.Model):
    content = models.CharField(max_length = 500)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# Create your models here.
