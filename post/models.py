from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250,null=False,blank=False)
    date_created = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=2000)
    def __str__(self):
        return "%s" % self.title