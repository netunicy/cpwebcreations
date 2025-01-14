from pathlib import Path
import base64
BASE_DIR = Path(__file__).resolve().parent.parent
from .models import Logo, Mainimage,Tools_images
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
import mailtrap as mt


def homepage(request):
    image1=Logo.objects.all().values()
    tools=Tools_images.objects.all().values()
    image2 = Mainimage.objects.filter(id=1).values()
    image3 = Mainimage.objects.filter(id=2).values()
    image4 = Mainimage.objects.filter(id=3).values()
    image5 = Mainimage.objects.filter(id=4).values()
    #viewer, created = PageView.objects.get_or_create(pk=1)
    #viewer.homepage_view_count += 1
    #viewer.save()

    context={
        'logo':image1,
        'image1':image2,
        'image2':image3,
        'image3':image4,
        'image4':image5,
        #'viewer': viewer.homepage_view_count,
        'tools':tools,
    }
    return render(request,'homepage.html',context)

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # Ανάκτηση δεδομένων φόρμας
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data.get('phone', 'N/A')
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            uploaded_file = form.cleaned_data.get('file')

            # Έλεγχος αν το αρχείο υπάρχει και αν είναι PDF
            if uploaded_file is None or not uploaded_file.name.endswith('.pdf'):
                form.add_error('file', 'The file must be in PDF format.')
                return render(request, 'contact_us_form.html', {'form': form})

            # Έλεγχος αν το αρχείο είναι πολύ μεγάλο (π.χ., > 10 MB)
            if uploaded_file.size > 10 * 1024 * 1024:  # 10 MB
                form.add_error('file', 'The uploaded file is too large. Maximum size allowed is 10MB.')
                return render(request, 'contact_us_form.html', {'form': form})

            try:
                # Διαβάστε το περιεχόμενο του αρχείου και κωδικοποιήστε το
                pdf_content = uploaded_file.read()
                pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')

                # Δημιουργία attachment
                pdf_attachment = mt.Attachment(
                    content=pdf_base64,
                    filename=uploaded_file.name,
                    mimetype="application/pdf",
                )

                # Δημιουργία email
                mail = mt.Mail(
                    sender=mt.Address(email="hello@cpsoftwarecreation.com", name="Contact Us"),
                    to=[mt.Address(email="cpsoftwarecreation@outlook.com")],
                    bcc=[mt.Address(email="charalampospitris1983@gmail.com")],
                    subject=subject,
                    text=f"{name} {surname}\n{phone}\n{email}\n{message}",
                )
                mail.attachments = [pdf_attachment]

                # Αποστολή email
                client = mt.MailtrapClient(token="386e1cd7d9a0bf8c155fa1204e037903")
                client.send(mail)

                # Εμφάνιση μηνύματος επιτυχίας
                messages.add_message(request, messages.INFO, 'Your message has been successfully sent. We will get back to you within 2 business days at the latest.')
                return render(request, "homepage.html", {"message": message})

            except Exception as e:
                form.add_error(None, f"Failed to send email: {str(e)}")
                return render(request, 'contact_us_form.html', {'form': form})

        else:
            return render(request, "contact_us_form.html", {"form": form})

    # GET request: Επιστροφή φόρμας
    else:
        form = ContactForm()

    return render(request, "contact_us_form.html", {'form': form})


