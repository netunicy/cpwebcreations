from django.shortcuts import render
from .models import Logo, Mainimage
from django.shortcuts import redirect, render
#from .models import Contact
import mailtrap as mt


def homepage(request):
    image1=Logo.objects.all().values()
    image2 = Mainimage.objects.filter(id=1).values()
    image3 = Mainimage.objects.filter(id=2).values()
    image4 = Mainimage.objects.filter(id=3).values()
    image5 = Mainimage.objects.filter(id=4).values()

    context={
        'logo':image1,
        'image1':image2,
        'image2':image3,
        'image3':image4,
        'image4':image5,
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
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    email = request.POST.get('email')
    phone = request.POST.get('phonenum')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    
    mail = mt.Mail(
      sender=mt.Address(email="mailtrap@cpnetuni.com", name="Contact"),
      to=[mt.Address(email='cpsoftwaresolutions@outlook.com')],
      subject=subject,
      text = name + ' ' + surname + '\n' + phone + '\n' +email + '\n' + message,
      category="Contact",
    )
    client = mt.MailtrapClient(token="3a3a19708b13ce12b954eab968ee3a59")
    client.send(mail)
    name = None
    surname = None
    email = None
    phone = None
    subject = None
    message = None
    return redirect ('cpsoftware')
  else:
    return render(request, "contact_us_form.html")