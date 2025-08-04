from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.conf import settings
from .forms import ContactForm

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

        html_content = render_to_string(
            'booking_emails/booking_data_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        message = EmailMessage(
            subject=subject,
            body=html_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[os.environ.get("ADMIN_EMAIL")]
        )

        message.content_subtype = "html"

        try:
            message.send()
            print("Admin booking data email sent successfully.")
        except Exception as e:
            print(f"Error sending admin email: {e}")

    def _send_confirmation_email(self, order):
        cust_email = order['email']
        subject = render_to_string(
            'booking_emails/booking_email_subject.txt',
            {'order': order}
        )

        html_content = render_to_string(
            'booking_emails/booking_email_body.txt',
            {'order': order, 'contact_email': settings.ADMIN_EMAIL}
        )

        message = EmailMessage(
            subject=subject,
            body=html_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[cust_email]
        )
        message.content_subtype = "html"

        try:
            message.send()
            print("Confirmation email sent to customer successfully.")
        except Exception as e:
            print(f"Error sending confirmation email: {e}")

    def form_valid(self, form):
        form.save()
        data = form.cleaned_data
        self._send_booking_data(data)
        self._send_confirmation_email(data)
        return super().form_valid(form)
