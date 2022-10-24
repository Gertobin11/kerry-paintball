from django.views.generic import ListView, DetailView
from .models import Package


class Packages(ListView):
    model = Package


class PackageDetail(DetailView):
    model = Package
