from django.db import models

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
    content=models.TextField(max_length=10000,null=True,blank=True)
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
    
class Tools_images(models.Model):
    image1=models.CharField(max_length=1000, null=True, blank=True)
    image2=models.CharField(max_length=1000, null=True, blank=True)
    image3=models.CharField(max_length=1000, null=True, blank=True)
    image4=models.CharField(max_length=1000, null=True, blank=True)
    image5=models.CharField(max_length=1000, null=True, blank=True)
    image6=models.CharField(max_length=1000, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Tools Images'
    
    def __str__(self):
        return 'Tools Images'
    
#from django.db import models


#class Contact(models.Model):
    #name=models.CharField(max_length=200, blank=False)

    #surname=models.CharField(max_length=200, blank=False)

    #email=models.EmailField(max_length=50, blank=False)
    
    #phone=models.CharField(max_length=50, blank=False)

    #subject = models.TextField(max_length=50, blank=False)

    #message =models.TextField(max_length=500, blank=False)

    #def __str__(self):
        #return self.name
