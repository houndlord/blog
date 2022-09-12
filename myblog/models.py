from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=32, unique=True)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    publish_date = models.DateField()
    tags = Tag.tag
    url = models.CharField(max_length=32, null=True)

    class Meta:     
        ordering = ['publish_date']  

    def __str__(self):
        return self.body
