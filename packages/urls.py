from django.urls import path
from .views import Packages

urlpatterns = [
    path('', Packages.as_view(), name='packages')
]
