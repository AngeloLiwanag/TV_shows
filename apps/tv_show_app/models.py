from __future__ import unicode_literals
from django.db import models

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len (postData['title']) < 2:
            errors['title'] = 'Title name should be at least 2 characters'
        if len(postData['network']) < 3:
            errors['network'] = 'Network should be at least 10 characters'
        return errors

class user(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.TextField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)
    objects = userManager()


    def __repr__(self):
        f"{self.title} {self.network} {self.release_date} {self.desc}"



# Create your models here.
