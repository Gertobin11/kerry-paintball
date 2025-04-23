from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string

from django.conf import settings
from .forms import ContactForm

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
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

        message = Mail(
            from_email=os.environ.get('EMAIL_SENDER'),
            to_emails=[os.environ.get("ADMIN_EMAIL")],
            subject=subject,
            html_content=body)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

    def form_valid(self, form):
        form.save()
        data = form.cleaned_data
        self._send_booking_data(data)
        return super().form_valid(form)
