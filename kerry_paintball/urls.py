from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include("home.urls")),
    path('packages/', include('packages.urls')),
    path('contact/', include('contact.urls')),
    path('gallery/', include('gallery.urls')),
    path('info/', include('info.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
