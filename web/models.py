from email import message
from email.headerregistry import Address
from operator import mod
from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField


class Gallery(models.Model):
    title = models.CharField(max_length=129)
    image = VersatileImageField('Image',upload_to='gallery/')
    
    class Meta:
        verbose_name_plural = ("Gallery")

    def __str__(self):
        return str(self.title)


class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    email=models.EmailField()
    message = models.TextField()

    def __str__(self):
        return str(self.name)