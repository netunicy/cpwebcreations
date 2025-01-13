from django.shortcuts import render
from .models import Logo, Mainimage, PageView,Tools_images
from django.shortcuts import redirect, render
from django.contrib import messages
import mailtrap as mt
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
import mailtrap as mt
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm


def homepage(request):
    image1=Logo.objects.all().values()
    tools=Tools_images.objects.all().values()
    image2 = Mainimage.objects.filter(id=1).values()
    image3 = Mainimage.objects.filter(id=2).values()
    image4 = Mainimage.objects.filter(id=3).values()
    image5 = Mainimage.objects.filter(id=4).values()
    viewer, created = PageView.objects.get_or_create(pk=1)
    viewer.homepage_view_count += 1
    viewer.save()

    context={
        'logo':image1,
        'image1':image2,
        'image2':image3,
        'image3':image4,
        'image4':image5,
        'viewer': viewer.homepage_view_count,
        'tools':tools,
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

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Ανάκτηση δεδομένων φόρμας
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data.get('phone', 'N/A')
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            mail = mt.Mail(
            sender=mt.Address(email="hello@cpsoftwarecreation.com", name="Contact Us"),
            to=[mt.Address(email="cpsoftwarecreation@outlook.com")],
            subject=subject,
            text=f"{name} {surname}\n{phone}\n{email}\n{message}",
            category="Contact Us",
            )

            client = mt.MailtrapClient(token="386e1cd7d9a0bf8c155fa1204e037903")
            client.send(mail)
            name = None
            surname = None
            email = None
            phone = None
            subject = None
            message = None
            messages.add_message(request, messages.INFO, 'Your message has been successfully sent. We will get back to you within 2 business days at the latest.')
            return render(request, "homepage.html", {"message": message})
        else:
            return render(request, "contact_us_form.html", {"form": form})

            
  # Redirect σε success page
    else:
        form = ContactForm()

    return render(request, "contact_us_form.html", {'form': form})

