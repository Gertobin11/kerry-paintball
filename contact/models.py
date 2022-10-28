import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator

GROUP_CHOICES = (('Stag', 'Stag'), ('Adults', 'Adults'),
                 ('Corporate', 'Corporate'), ('Teens', 'Teens'),
                 ('School', 'School'), ('Splatball', 'Splatball'))


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    booking_type = models.CharField(choices=GROUP_CHOICES, max_length=30)
    number_of_players = models.IntegerField(default=10,
                                            validators=[MaxValueValidator(120),
                                                        MinValueValidator(1)])
    date_to_play = models.DateField(validators=[MinValueValidator(
                                    datetime.date.today)])
    time_to_play = models.TimeField()
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

