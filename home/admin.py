from django.contrib import admin
from . import models

class ContactInformationPhoneInline(admin.TabularInline):
    model = models.ContactInformationPhone
    extra = 1

class ContactInformationAdmin(admin.ModelAdmin):
    inlines = [ContactInformationPhoneInline]

class AboutUsAdditionInline(admin.TabularInline):
    model = models.AboutUsAddition
    extra = 2

class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsAdditionInline]


admin.site.register(models.ContactUs)
admin.site.register(models.ContactInformation, ContactInformationAdmin)
admin.site.register(models.AboutUs, AboutUsAdmin)
