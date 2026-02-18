from django.contrib import admin
from .models import User, UserProfile
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_staff', 'is_active', 'created_at', 'updated_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-created_at',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name_th', 'last_name_th', 'first_name_en', 'last_name_en', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'first_name_th', 'last_name_th', 'first_name_en', 'last_name_en')
    ordering = ('-created_at',)
