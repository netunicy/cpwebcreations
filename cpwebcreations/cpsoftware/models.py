from django.db import models
from tinymce.models import HTMLField

class PageView(models.Model):
    homepage_view_count = models.IntegerField(default=0)

class Logo(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    image=models.CharField(max_length=1000, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Logo'
    
    def __str__(self):
        return self.name
    
class Mainimage(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    image=models.CharField(max_length=1000, null=True, blank=True)
    content=HTMLField(null=True,blank=True)
    class Meta:
        verbose_name_plural = 'Main Image'
    
    def __str__(self):
        return self.name

class Aboutus(models.Model):
    title=models.CharField(max_length=500,null=True,blank=True)
    text=models.TextField(max_length=2000,null=True,blank=True)
    class Meta:
        verbose_name_plural = 'About Us'
    
    def __str__(self):
        return self.title