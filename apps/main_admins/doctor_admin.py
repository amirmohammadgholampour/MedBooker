from django.contrib import admin 
from apps.main_models.doctor_models import Doctor 

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["full_name", "expertise", "city", "medical_code", "office_phone", "website", "created_at"]
    list_filter = ["expertise", "city"]
    search_fields = ["doctor_user__first_name", "doctor_user__last_name", "doctor_user__username", "medical_code"]
    readonly_fields = ["created_at", "updated_at"]
    autocomplete_fields = ["doctor_user"]
    list_per_page = 10
    ordering = ["-created_at"]

    def full_name(self, obj):
        return f"{obj.doctor_user.first_name} {obj.doctor_user.last_name}"
    full_name.short_description = "Doctor Name"
