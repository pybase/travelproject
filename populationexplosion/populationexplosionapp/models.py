from django.db import models


# Create your models here
class places(models.Model):
    img = models.ImageField(upload_to='pics')

    place_name = models.CharField(max_length=250)
    place_descp = models.TextField()

    def __str__(self):
        return self.place_name


class members(models.Model):
    img1 = models.ImageField(upload_to='photos')
    name = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.name

