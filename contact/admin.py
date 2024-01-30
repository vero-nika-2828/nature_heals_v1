from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    display = {
        'name',
        'email',
        'message',
        'created_date ',
    }


admin.site.register(Contact, ContactAdmin)
