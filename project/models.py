from django.db import models

class ModelAnna(models.Model):
    pole = models.TextField()
    email = models.CharField(max_length=15)
    password = models.CharField(max_length=50)

class ModelEgor(models.Model):

    name = models.CharField(max_length=10)
    email = models.CharField(max_length=15)
    password = models.CharField(max_length=30)


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title