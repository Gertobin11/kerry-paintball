from .models import Package


def all_packages(request):
    packages = Package.objects.all()
    context = {
        'packages': packages
    }
    return context
