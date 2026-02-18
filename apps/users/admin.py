from django.contrib import admin
from .models import User, UserProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('username', 'email')
    ordering = ('-created_at',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name_th', 'last_name_th', 'first_name_en', 'last_name_en', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user_id__username', 'user_id__email', 'first_name_th', 'last_name_th', 'first_name_en', 'last_name_en')
    ordering = ('-created_at',)
