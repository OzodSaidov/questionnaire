from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        ('User information', {
            'fields': ('username', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2',),
        }),
    )

    save_on_top = True
    # readonly_fields = ('user_ident', 'username')
