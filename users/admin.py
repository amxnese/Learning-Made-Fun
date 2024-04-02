from django.contrib import admin
# from .models import Member
# admin.site.register(Member)

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define the fields to be displayed in the user list
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
