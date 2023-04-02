from django.db import models

# Create your models here.

class HomeName(models.Model):

    name = models.CharField('Home name', max_length=50)

    def __str__(self):
        return self.name

class HomeVideo(models.Model):

    video = models.FileField('Home video', upload_to='videos')

class Subtitle(models.Model):

    name = models.CharField('Subtitle name', max_length=50)

    def __str__(self):
        return self.name
    
class Content(models.Model):

    img = models.ImageField('Content image', upload_to='images')
    name = models.CharField('Content name', max_length=60)
    text = models.TextField('Content text')
    date = models.DateTimeField('Content date', auto_now=True)

    def __str__(self):
        return self.name
    
class About(models.Model):

    name = models.CharField('About name', max_length=60)
    text = models.TextField('About text')


class Contact(models.Model):

    contact_name = models.CharField('Contact name', max_length=60)
    contact_email = models.EmailField('Contact Email')
    contact_message = models.TextField('Contact text')

    def __str__(self):
        return self.contact_name