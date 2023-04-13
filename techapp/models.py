from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100,blank=False, null=False)
    discription = models.TextField(blank=False,null=False)
    
    def __str__(self):
        return self.title
