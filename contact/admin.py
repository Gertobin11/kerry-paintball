from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):

    model = Contact

    search_fields = ['first_name', 'email', 'last_name']
    list_filter = ['booking_type']

    list_display = ['first_name', 'last_name', 'booking_type', 'date_to_play']
    ordering = ('-created',)


admin.site.register(Contact, ContactAdmin)
