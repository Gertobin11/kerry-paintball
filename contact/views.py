from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm


class Contact(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = '/'
    success_message = ('Your enquiry has been successfully '
                       'recieved,we will be in contact shortly')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
