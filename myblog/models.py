from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    publish_date = models.DateField()
    tags = models.CharField(max_length=64)
    url = models.CharField(max_length=32, null=False)

    class Meta:     
        ordering = ['publish_date']  

    def __str__(self):
        return self.body
