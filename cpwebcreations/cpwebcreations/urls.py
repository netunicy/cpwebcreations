from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cpsoftware.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('captcha/', include('captcha.urls')),
    path('favicon.ico', RedirectView.as_view(url='/staticfiles/favico/favicon.ico')),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
