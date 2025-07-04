from django.contrib import admin
from apps.main_models.appointment_models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        "appointment_info",
        "doctor_name",
        "patient_name",
        "status",
        "date",
        "start_time",
        "end_time",
        "created_at"
    ]
    list_filter = ["status", "date", "doctor__doctor_user__last_name"]
    search_fields = [
        "doctor__doctor_user__first_name",
        "doctor__doctor_user__last_name",
        "patient__first_name",
        "patient__last_name"
    ]
    ordering = ["-date", "start_time"]
    list_per_page = 15
    autocomplete_fields = ["doctor", "patient"]
    readonly_fields = ["created_at", "updated_at"]

    def doctor_name(self, obj):
        return f"Dr. {obj.doctor.doctor_user.last_name}"
    doctor_name.short_description = "Doctor"

    def patient_name(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"
    patient_name.short_description = "Patient"

    def appointment_info(self, obj):
        return f"{obj.date} - {obj.start_time}"
    appointment_info.short_description = "Appointment"