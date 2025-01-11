from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cpsoftware.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('captcha/', include('captcha.urls')),
    path('favicon.ico', RedirectView.as_view(url='/staticfiles/favico/favicon.ico')),
]
