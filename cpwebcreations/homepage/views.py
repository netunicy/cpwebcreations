from django.shortcuts import render
from .models import Logo, Mainimage

def homepage(request):
    image=Logo.objects.all().values()
    image2=Mainimage.objects.all().values()

    context={
        'logo':image,
        'image':image2,
    }
    return render(request,'homepage.html',context)


def aboutus(request):
    #about_us=Aboutus.objects.all().values()
    image=Logo.objects.all().values()
    context = {
        #'about_us':about_us,
        'logo':image,
    }
    return render(request,'about_us.html',context)
