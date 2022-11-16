from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from packages.models import Package
from .sitemaps import StaticViewSitemap

info_dict = {
    'queryset': Package.objects.all()
}
sitemaps = {
    'package': GenericSitemap(info_dict, priority=0.9),
    'generic': StaticViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include("home.urls")),
    path('packages/', include('packages.urls')),
    path('contact/', include('contact.urls')),
    path('gallery/', include('gallery.urls')),
    path('info/', include('info.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
