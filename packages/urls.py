from django.urls import path
from .views import Packages, PackageDetail

urlpatterns = [
    path('', Packages.as_view(), name='packages'),
    path('<int:pk>/', PackageDetail.as_view(), name='package_detail')
]
