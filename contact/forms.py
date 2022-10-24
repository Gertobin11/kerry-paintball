from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from captcha.fields import CaptchaField
from django.forms import ModelForm, widgets
from .models import Contact


class ContactForm(ModelForm):
    phone_number = PhoneNumberField(region="FR",
                                    widget=PhoneNumberPrefixWidget(
                                        initial="IE",
                                        country_choices=[
                                            ("IE", "Ireland"),
                                            ("UK", "UK"),
                                        ],)
                                    )
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'date_to_play': widgets.DateInput(attrs={'type': 'date'}),
            'time_to_play': widgets.TimeInput(attrs={'type': 'time'})
        }
