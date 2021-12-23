from django.db import models

# Create your models here.


class Import_Data(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=50)
    price = models.IntegerField()
    company = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}, {self.unit}, {self.price}'


class Exeldocument(models.Model):
    doc = models.FileField()
