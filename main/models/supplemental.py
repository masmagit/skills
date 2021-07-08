from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=80)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True, related_name='countries')

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=80)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, blank=True, related_name='cities')

    def __str__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name