from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('contact_us/',views.contact_us, name='contact_us'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)