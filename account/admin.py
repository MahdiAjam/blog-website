from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from .models import User, OtpCode


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'full_name', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        ('main', {'fields': ('email', 'phone_number', 'full_name', 'image', 'description', 'password')}),
        ('permissions', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )

    add_fieldsets = (
        ('Add user', {'fields': ('phone_number', 'email', 'full_name', 'password1', 'password2', 'is_admin', 'is_active')}),
    )

    search_fields = ('email', 'full_name',)
    ordering = ('full_name',)
    filter_horizontal = ()

@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
