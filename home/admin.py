from django.contrib import admin
from . import models

class ContactInformationPhoneInline(admin.TabularInline):
    model = models.ContactInformationPhone
    extra = 1

class ContactInformationAdmin(admin.ModelAdmin):
    inlines = [ContactInformationPhoneInline]

admin.site.register(models.ContactUs)
admin.site.register(models.ContactInformation, ContactInformationAdmin)
