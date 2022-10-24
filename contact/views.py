from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.conf import settings
from .forms import ContactForm


class Contact(SuccessMessageMixin, CreateView):
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = '/'
    success_message = ('Your enquiry has been successfully '
                       'recieved,we will be in contact shortly')

    def _send_confirmation_email(self, order):
        # Send the user a confirmation email
        cust_email = order['email']
        subject = render_to_string(
            'booking_emails/booking_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'booking_emails/booking_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(
            subject,
            body,
            'test@test.ie',
            [cust_email]
        )

    def _send_booking_data(self, order):
        # Send Admin booking enquiry details
        admin_email = order['email']
        subject = render_to_string(
            'booking_emails/booking_data_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'booking_emails/booking_data_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(
            subject,
            body,
            'test@test.ie',
            [admin_email]
        )

    def form_valid(self, form):
        form.save()
        data = form.cleaned_data
        self._send_confirmation_email(data)
        self._send_booking_data(data)
        return super().form_valid(form)
