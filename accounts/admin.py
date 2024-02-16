from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # passing default user model form security feature

from accounts.models import User
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'role', 'status', 'latitude', 'longitude', 'place']  # Add extra fields here
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'role', 'status', 'latitude', 'longitude', 'place')}),  # Add agin extra fields here
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups')}
        ),
    )

# Re-register UserAdmin
admin.site.register(User, CustomUserAdmin)