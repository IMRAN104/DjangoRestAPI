from django.db import models


# Create your models here.
class Blogpost(models.Model):
    post_title = models.CharField(null=True, blank=True, max_length=100)
    psot_desscription = models.TextField(
        null=True, blank=True, max_length=1000)

    def __str__(self):
        return self.post_title
