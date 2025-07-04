from django.contrib import admin 
from apps.main_models.doctor_schedule_models import DoctorSchedule 

@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = ["doctor_name", "days_week", "start_time", "end_time", "is_available", "gap_between_slots", "slot_duration"]
    list_filter = ["is_available", "days_week"]
    search_fields = ["doctor__doctor_user__first_name", "doctor__doctor_user__last_name"]
    ordering = ["-created_at"]
    list_per_page = 10
    autocomplete_fields = ["doctor"]
    readonly_fields = ["created_at", "updated_at"]

    def doctor_name(self, obj):
        return f"{obj.doctor.doctor_user.first_name} {obj.doctor.doctor_user.last_name}"
    doctor_name.short_description = "Doctor"