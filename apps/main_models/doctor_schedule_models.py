from django.db import models 
from apps.main_models.doctor_models import Doctor 

class DaysWeek(models.TextChoices):
    MONDAY = "monday", "Monday"
    TUESDAY = "tuesday", "Tuesday"
    WEDNESDAY = "wednesday", "Wednesday"
    THURSDAY = "thursday", "Thursday"
    FRIDAY = "friday", "Friday"
    SATURDAY = "saturday", "Saturday"
    SUNDAY = "sunday", "Sunday"


class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="schedules")
    
    days_week = models.CharField(max_length=10, choices=DaysWeek.choices, verbose_name="Day of Week")
    
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    is_available = models.BooleanField(default=True)
    
    gap_between_slots = models.PositiveIntegerField(default=0, help_text="Break between each appointment (in minutes)")
    slot_duration = models.PositiveIntegerField(default=15, help_text="Duration of each appointment slot in minutes")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.doctor.doctor_user.first_name} - {self.days_week} ({self.start_time} to {self.end_time})"