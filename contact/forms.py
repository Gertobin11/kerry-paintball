from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm, widgets
from .models import Contact


class ContactForm(ModelForm):
    phone_number = PhoneNumberField()

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'date_to_play': widgets.DateInput(attrs={'type': 'date'}),
            'time_to_play': widgets.TimeInput(attrs={'type': 'time'})
        }
