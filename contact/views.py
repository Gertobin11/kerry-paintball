from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.conf import settings
from .forms import ContactForm
import logging
import smtplib

logger = logging.getLogger()


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

        logger.info(f"Attempting to send booking email for contact form submission.")
        logger.debug(f"Email Subject: '{subject}'")

        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            logger.info("email sent successfully")

        except smtplib.SMTPException as e:
            logger.error(f"SMTP error sending booking email: {e}", exc_info=True)

        except Exception as e:
            logger.error(f"Unexpected error sending booking email: {e}", exc_info=True)

    def form_valid(self, form):
        form.save()
        data = form.cleaned_data
        self._send_booking_data(data)
        return super().form_valid(form)
