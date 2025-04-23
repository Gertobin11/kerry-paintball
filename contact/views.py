from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.conf import settings
from .forms import ContactForm
from yagmail import SMTP
import os


class Contact(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = '/'
    success_message = ('Your enquiry has been successfully '
                       'recieved,we will be in contact shortly')

    def _send_booking_data(self, order):
        # Send Admin booking enquiry details
        subject = render_to_string(
            'booking_emails/booking_data_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'booking_emails/booking_data_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        yag = SMTP(os.environ.get("EMAIL_HOST_USER"), os.environ.get("EMAIL_HOST_PASSWORD"))
        yag.send(os.environ.get("ADMIN_EMAIL"), subject, body)

    def form_valid(self, form):
        form.save()
        data = form.cleaned_data
        self._send_booking_data(data)
        return super().form_valid(form)
