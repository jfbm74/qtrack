from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'bio']  # Ajusta los campos que necesitas mostrar

admin.site.register(UserProfile, UserProfileAdmin)
