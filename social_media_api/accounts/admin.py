from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """ extending the default userAdmin to show our extra fields."""

    fieldsets = BaseUserAdmin.fieldsets + (
        ("profile", {"fields": ("bio", "profile_picture", "followers")}),
    )
    list_display = ("username", "email", "is_staff", "is_active")
    search_fields = ("username", "email")