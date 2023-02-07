from email import message
from email.headerregistry import Address
from operator import mod
from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField


class Portfolio(models.Model):
    title = models.CharField(max_length=129)
    image = VersatileImageField('Image',upload_to='portfolio/')
    
    class Meta:
        verbose_name_plural = ("Portfolio")

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



class Update(models.Model):
    title=models.CharField(max_length=225)
    summary=models.CharField(max_length=500)
    date=models.DateField()
    image=VersatileImageField('Image',upload_to='updates/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')
    content=HTMLField(blank=True, null=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return str(self.title)



class FAQ(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return str(self.question)

    class Meta:
        verbose_name_plural = ("FAQ")



class Banner(models.Model):
    category = models.CharField(max_length=50)
    title_first_word = models.CharField(max_length=100)
    title_second_word = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image=VersatileImageField('Image',upload_to='Banner/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return str(self.title_first_word)

    class Meta:
        verbose_name_plural = ("Banner")


class SocialMedia(models.Model):
    image=VersatileImageField('Image',upload_to='Banner/',ppoi_field='ppoi' )
    ppoi = PPOIField('Image PPOI')
    link=models.URLField()

    def __str__(self):
        return str(self.link)

    class Meta:
        verbose_name_plural = ("Social Media")
    

class SeoHome(models.Model):
    title = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=500)
    meta_title = models.CharField(max_length=500)
    meta_description = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = ("SEO Home")


class SeoAbout(models.Model):
    title = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=500)
    meta_title = models.CharField(max_length=500)
    meta_description = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = ("SEO About")


class SeoServices(models.Model):
    title = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=500)
    meta_title = models.CharField(max_length=500)
    meta_description = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = ("SEO Services")


class SeoPortfolio(models.Model):
    title = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=500)
    meta_title = models.CharField(max_length=500)
    meta_description = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = ("SEO Portfolio")


class SeoBlog(models.Model):
    title = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=500)
    meta_title = models.CharField(max_length=500)
    meta_description = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = ("SEO Blog")


class SeoContact(models.Model):
    title = models.CharField(max_length=200)
    meta_keywords = models.CharField(max_length=500)
    meta_title = models.CharField(max_length=500)
    meta_description = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = ("SEO Contact")