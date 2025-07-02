from django.contrib import admin, messages
from apps.main_models.user_models import User 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

def make_active(modeladmin, request, queryset):
    active = queryset.update(is_active=True)
    messages.success(request, f"{active} Activate selected users.") 

class UserAdmin(BaseUserAdmin):
    model = User 
    actions = [make_active]
    list_display = [
        "username", 
        "phone_number", 
        "national_code",
        "is_staff",
        "is_active",
        "first_name", 
        "last_name",
        "email",
        "gender",
        "birth_date",
        "user_type"
    ]

    list_filter = [
        "is_staff",
        "is_active",
        "user_type"
    ]

    fieldsets = (
        (None, {"fields": ("phone_number", "username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "gender", "national_code", "user_type")}),
        ("Accesses", {"fields": ("is_staff", "is_active", "is_superuser", "groups")}),
        ("Date", {"fields": ("join_date",)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("username", "email", "national_code", "user_type", "password1", "password2", "is_superuser", "is_staff", "is_active")}
        ),
    )

    search_fields = ("phone_number", "national_code", "username")
    ordering = ["-join_date"]

admin.site.register(User, UserAdmin) 