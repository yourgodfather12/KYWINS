from django.db import models
from django.contrib.auth.models import User

class County(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Girl(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Image(models.Model):
    girl = models.ForeignKey(Girl, on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Image of {self.girl.name}"
