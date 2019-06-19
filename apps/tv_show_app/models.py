from django.db import models

class user(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.TextField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        f"{self.title} {self.network} {self.release_date} {self.desc}"
# Create your models here.
